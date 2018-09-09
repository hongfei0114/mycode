# 二级路由

from django.conf.urls import url
from fault_reporting import views

urlpatterns = [

    # # 第一版 二级路由 全部分开写
    # url('^lob/(.*)$', views.lob),
    # url('^tag/(.*)$', views.tag),
    # url('^archive/(.*)$', views.archive),

    # # 第二版 二级路由 三合一
    # url('^(lob|tag|archive)/(.*)$', views.sanheyi),  # Sanheyi(request,*args)

    # 第三版 二级路由 四合一
    url('^(lob|tag|archive)/(.*)/$', views.index),  # Sanheyi(request, 'lob', '游戏')

    url('^$', views.index),
]
