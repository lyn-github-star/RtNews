import xadmin
from django.contrib import admin
from xadmin import views
from news_app.models import Type, UserInfo, Comment, Content


# Register your models here.
# 设置admin
class TypeAdmin:
    # 数据添加列表显示字段
    list_display = ['id', 'name']
    # 添加搜索功能
    search_fields = ['id', 'name']
    # 排序功能
    list_filter = ['id', 'name']
    ordering = ['id']


# class UserInfoAdmin:
#     # 数据添加列表显示字段
#     list_display = ['id', 'username', 'nickname', 'gender', 'email', 'mobile']
#     # 添加搜索功能
#     search_fields = ['id', 'username', 'nickname', 'gender', 'email', 'mobile']
#     list_filter = ['id', 'username', 'nickname', 'gender', 'email', 'mobile', 'birthday']
#     # 排序功能
#     ordering = ['id']
#     list_per_page = 10


class ContentAdmin:
    list_display = ['id', 'title', 'picture', 'publish_time']
    # 添加搜索功能
    search_fields = ['id', 'title', 'picture', 'publish_time']
    # shaixuan
    list_filter = ['id', 'title', 'picture', 'publish_time']
    # 排序功能
    ordering = ['id']
    list_per_page = 10


class CommentAdmin:
    list_display = ['id', 'user_id', 'news_id', 'publish_time']
    # 添加搜索功能
    search_fields = ['id', 'user_id', 'news_id', 'publish_time']
    # shaixuan
    list_filter = ['id', 'user_id', 'news_id', 'publish_time']
    ordering = ['id']
    list_per_page = 10


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "人通新闻"
    site_footer = "河北人通科技有限公司"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将models 注册到admin
xadmin.site.register(Type, TypeAdmin)
# xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Content, ContentAdmin)
