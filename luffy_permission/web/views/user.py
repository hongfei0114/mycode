"""
跟用户相关的视图
"""

from django.shortcuts import render, redirect, HttpResponse
from rbac.models import UserInfo
from django.conf import settings


def login(request):
    error_msg = ""
    if request.method == 'POST':
        # 取数据
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        # 校验
        user_obj = UserInfo.objects.filter(username=username, password=pwd).first()
        if user_obj:
            # 登录成功
            # 拿到登录用户的所有权限
            ret = user_obj.roles.all().values("permissions__url").distinct
            # 保存ret到全局变量 ，存到session
            request.session[settings.PERMISSION_SESSION_KEY] = list(ret)
            return redirect('/customer/list/')

        else:
            # 登录失败
            error_msg = "用户名或密码错误"

            pass

    return render(request, 'login.html', {'error_msg': error_msg})
