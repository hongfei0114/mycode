"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/', views.login),
    url(r'^user_list/', views.user_list),
    url(r'^delete_user/(?P<delid>\d+)/$', views.DeleteUser.as_view()),
    url(r'^reset_pass/(?P<reset_id>\d+)/$', views.ResetPass.as_view()),
    url(r'^register/', views.register),

    url(r'^check_user/', views.check_user),
    url(r'^check_pass/', views.check_pass),
    url(r'^check_pass_confirm/', views.check_pass_confirm),

    url(r'^service_list/', views.ServiceList.as_view()),
    url(r'^$', views.ServiceList.as_view()),
    url(r'^add_service/', views.AddService.as_view()),
    url(r'^del_service/(\d+)', views.DelService.as_view()),
    url(r'^config_service/(\d+)', views.ConfigService.as_view()),

    url(r'^hosts_list/', views.HostsList.as_view()),
    url(r'^delete_hosts/(\d+)', views.DeleteHosts.as_view()),
    url(r'^config_hosts/(\d+)', views.ConfigHosts.as_view()),
    url(r'^add_hosts/', views.AddHosts.as_view()),

]

