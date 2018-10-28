"""
自定义RBAC中间件
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse
import re
from django.conf import settings


class RBACMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        自定义权限校验的中间件
        :param request: 请求对象
        :return:
        """
        # 1. 取到当前这次请求访问的URL是什么
        url = request.path_info  # request.get_full_path()
        # 1.5 进行白名单过滤
        for item in settings.PERMISSION_WHITE_URL:
            reg = "^{}$".format(item)
            if re.match(reg, url):
                return None
        # 2. 取到当前用户的权限列表
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY, None)
        # 3. 进行权限校验
        if permission_list is None:
            # 该用户没登陆
            return redirect("/login/")
        print("=" * 120)
        # 循环当前用户的所有权限
        for i in permission_list:
            # 注意要使用全匹配模式
            reg = "^{}$".format(i['permissions__url'])
            if re.match(reg, url):
                break
                # return None  # 只要匹配上就跳出循环
        else:
            # 在我的权限列表里就没找到和你访问的URL匹配的，说明没有权限
            return HttpResponse("滚~")
