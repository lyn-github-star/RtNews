import hashlib
import re
import random

from django.views import View

from RtNews.settings import APIKEY
from untils.yunpian import YunPian
from news_app.models import VerifyCode
from django.http import HttpResponse
from news_app import models
from django.shortcuts import render, redirect
from news_app.models import Type, Content, UserInfo
from news_app.forms import UserForm, RegisterForm
from yunpian import send_sms


# Create your views here.
def index(request):
    new_type = Type.objects.all()
    type_id = request.GET.get("type_id", None)
    search = request.GET.get("search", None)
    if search is not None:
        content = Content.objects.filter(title__icontains=search)
        return render(request, "index.html", locals())
    if type_id:
        content = Content.objects.filter(type_id=type_id)
    else:
        content = Content.objects.all()
    return render(request, "index.html", locals())


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.UserInfo.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            print("username:", username)
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            mobile = register_form.cleaned_data['mobile']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'signup.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'signup.html', locals())
                same_mobile_user = models.UserInfo.objects.filter(mobile=mobile)
                if same_mobile_user:  # 手机号地址唯一
                    message = '该手机地址已被注册，请使用别的手机号！'
                    return render(request, 'signup.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.UserInfo()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.mobile = mobile
                new_user.sex = sex
                new_user.save()
                return redirect('/login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'signup.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index")


# def lyn_xunhuan(request):
#     for i in range(100):
#         Content.objects.create(
#             type_id=Type.objects.get(id=4),
#             title="文章%s" % i, user_id=UserInfo.objects.get(id=1),
#             picture="测试")
#
#     return HttpResponse("ok")

class News(View):
    def get(self, request, content_id):
        types = Type.objects.all()
        data = Content.objects.get(id=content_id)
        data.clicked = int(data.clicked) + 1
        data.save()
        return render(request, "news.html", locals())


class ForCodeView(View):
    """获取手机验证码"""

    def get(self, request):
        return render(request, "yunpian.html")

    def post(self, request):
        mobile = request.POST.get('mobile', None)
        if mobile:
            # 验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 生成手机验证码
                result, code = send_sms(mobile)
                if result == 0:
                    ver = VerifyCode.objects.filter(mobile=mobile)
                    if ver:
                        ver[0].code = code
                        ver[0].save()
                    else:
                        VerifyCode.objects.create(
                            mobile=mobile,
                            code=code
                        )
                return HttpResponse(result)
            else:
                msg = '请输入有效手机号码!'
                return HttpResponse(msg)
        else:
            msg = '手机号不能为空！'
            return HttpResponse(msg)


class VerifyCodeHandel(View):
    def post(self, request):
        mobile = request.POST.get('mobile', None)
        code = request.POST.get('code', None)
        passwrod = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        mcode = VerifyCode.objects.get(mobile=mobile).code
        if mcode == code and passwrod == re_password:
            user = UserInfo.objects.get(mobile=mobile)
            user.password = hash_code(passwrod)
            user.save()
            return HttpResponse("YES")
        else:
            return HttpResponse("No")
