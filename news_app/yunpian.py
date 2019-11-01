from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
#
# # 初始化client,apikey作为所有请求的默认值
#
import random


def vier_key():
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'x', 'y',
                'z']
    veri_str = random.sample(list_str, 2)
    veri_num = random.sample(list_num, 2)
    veri_out = random.sample(veri_num + veri_str, 4)
    veri_res = str(veri_out[0]) + str(veri_out[1]) + str(veri_out[2]) + str(veri_out[3])
    return veri_res


def send_sms(phone):
    clnt = YunpianClient('f29eddaff34e6e6831e9192053a29bd6')
    key = vier_key()
    param = {YC.MOBILE: phone, YC.TEXT: f'您的验证码是{key}'}
    r = clnt.sms().single_send(param)
    return r.code(), key
    # 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
    # 短信:clnt.sms() 账户:clnt.user() 签名:clnt.sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()
#
#
# send_sms('17631736474', key())
