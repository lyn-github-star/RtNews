"""RtNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http import server

from django.conf.urls import url
from django.views.generic import TemplateView

import xadmin
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.views.static import serve
from news_app.views import index, login, register, logout, ForCodeView, VerifyCodeHandel, News

urlpatterns = [
    path('admin/', xadmin.site.urls),
    re_path('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('base/',TemplateView.as_view(template_name='base.html')),
    # path('index/',TemplateView.as_view(template_name='index.html')),
    # path('login/',TemplateView.as_view(template_name='login.html')),
    # path('news/<int:contend_id>/', News.as_view()),
    url(r"^news/(?P<content_id>\d+)", News.as_view()),
    # path('signup/',TemplateView.as_view(template_name='signup.html')),
    path('signup/', register),
    path('login/', login),
    path('logout/', logout),
    # path('lyn_xunhuan/',lyn_xunhuan),
    path('index/', index),
    path('forcode/', ForCodeView.as_view(), name='forcode'),
    url(r'^captcha/', include('captcha.urls')),
    path('sendcode/', VerifyCodeHandel.as_view())
]
