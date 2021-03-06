# _*_ encoding:utf-8 _*_
__author__ = 'zmbxzrq@outlook.com'
__date__ = '2019/2/1 11:09'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner
# 主题配置
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

# 后台页面配置
class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

# 后台注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)