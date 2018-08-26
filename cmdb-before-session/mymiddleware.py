from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time

D = {}
BLACK_LIST = ['/hosts_list/']


class LimitReq(MiddlewareMixin):

    def process_request(self, request):
        # print(request.META)
        ip = request.META.get("REMOTE_ADDR")
        now = time.time()

        if request.path_info not in BLACK_LIST:
            return None

        if ip not in D:
            D[ip] = []
        # 拿到当前ip的访问历史记录
        history = D[ip]
        # 不能遍历列表的同时又操作列表的元素个数
        # for record in history:
        #     if now - record > 60:

        while history and now - history[-1] > 10:
            history.pop()

        if len(history) >= 3:
            return redirect('/service_list/')
        else:
            history.insert(0, now)
