from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from faker import Faker
from ckeditor_uploader.fields import RichTextUploadingField



def get_nickname():
    fake = Faker()
    return fake.name()


# Create your models here.
# 新闻类型类
class Type(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="类型编号")
    name = models.CharField(max_length=64, verbose_name="姓名")

    def __str__(self):
        return "{name}".format(name=self.name)

    class Meta:
        db_table = "news_type"
        verbose_name = "新闻类型"
        verbose_name_plural = verbose_name


# 用户信息  继承自带的 User类
class UserInfo(AbstractUser):
    GENDER_CHOICES = (("0", "女"), ("1", "男"), ("2", "保密"))
    nickname = models.CharField(max_length=64, verbose_name="昵称", default=get_nickname())
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=2, verbose_name="性别")
    birthday = models.DateField(null=True, verbose_name="生日")
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name="电话")
    image = models.ImageField(max_length=255, upload_to="image/user/%Y/%m", default="user/default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "user_info"

    def __str__(self):
        return "{username}".format(username=self.username)


class Content(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号")
    user_id = models.ForeignKey(to="UserInfo", to_field="id", related_name="content", on_delete=models.DO_NOTHING)
    type_id = models.ForeignKey(to="Type", to_field="id", related_name="content", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=64, verbose_name="标题")
    picture = models.CharField(max_length=128, verbose_name="标签")
    content = RichTextUploadingField(verbose_name="评论")
    image = models.ImageField(max_length=255, upload_to="image/content/%Y/%m%d", default="content/default.jpg",
                              verbose_name="封面图片")
    publish_time = models.DateTimeField(default=datetime.now, verbose_name="生成时间")
    clicked = models.IntegerField(default=0, verbose_name="点击量")
    is_deleted = models.BooleanField(default=0, verbose_name="是否删除")

    def __str__(self):
        return "{title}".format(title=self.title)

    class Meta:
        db_table = "news_content"
        verbose_name = "新闻内容"
        verbose_name_plural = verbose_name


# 新闻评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="评论编号")
    user_id = models.ForeignKey(to="UserInfo", to_field="id", related_name='comment', null=True, blank=True,
                                on_delete=models.SET_NULL, verbose_name="评论用户")

    news_id = models.ForeignKey(to="Content", to_field="id", related_name="comment", on_delete=models.CASCADE,
                                verbose_name="新闻评论")
    content = RichTextUploadingField(verbose_name="评论内容")
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    is_deleted = models.BooleanField(default=0, verbose_name="是否删除")

    def __str__(self):
        return "{id}".format(id=self.id)

    class Meta:
        db_table = "news_comment"
        verbose_name = "新闻评论"
        verbose_name_plural = verbose_name


class VerifyCode(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='手机', unique=True)
    code = models.CharField(max_length=8, verbose_name='验证码')
    time = models.DateTimeField(auto_now=True, verbose_name='时间')

    class Meta:
        db_table = "verifycode"
        verbose_name = "手机验证"
        verbose_name_plural = verbose_name
