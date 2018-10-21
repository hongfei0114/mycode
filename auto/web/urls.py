from django.conf.urls import url,include
from web.views import home

urlpatterns = [
    url(r'^index/', home.index),
    url(r'^center/', home.center),
    # 用户相关
    url(r'^user/', home.user),
    url(r'^add_user/', home.add_user),
    url(r'^del_user/(\d+)', home.del_user),
    url(r'^edit_user/(\d+)', home.edit_user),
    # 订单相关
    url(r'^order/', home.order),
    url(r'^add_order/', home.add_order),
    url(r'^edit_order/(\d+)', home.edit_order),
    url(r'^del_order/(\d+)', home.del_order),

]
