
from django.conf.urls import url,include
from app01 import views
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^user/$', views.user_list),
    url(r'^center/$', views.center),
]

