"""
自定义rbac中间件
"""

from django.shortcuts import redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re
from django.conf import settings


class RBACMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        自定义权限校验的中间件
        :param request: 请求对象
        :return:
        """
        # 1. 取到这次请求访问的URL是什么
        url = request.path_info

        # 1.5 进行白名单的过滤 在配置文件中
        for item in settings.PERMISSION_WHITE_URL:
            reg = "^{}$".format(item)
            if re.match(reg, url):
                return None

        # 2. 取到当前用户的权限列表
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY, None)

        # 3. 进行权限校验
        if not permission_list:
            # 该用户没有登录
            return  redirect('/login/')

        for i in permission_list:
            reg = "^{}$".format(i['permissions_url'])
            if re.match(reg, url):
                break # 默认返回None
                # return None  # 不需要再走for循环
            else:
                return HttpResponse('滚')
