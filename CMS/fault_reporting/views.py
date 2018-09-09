from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
from fault_reporting import forms
from django.http import JsonResponse
from fault_reporting import models
from django.db.models import Count


# Create your views here.

class LoginView(views.View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        next_url = request.GET.get('next', '/index/')
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = auth.authenticate(username=username, password=pwd)
        if user_obj:
            auth.login(request, user_obj)
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误，请重新输入'})


def index(request, *args):
    lob_list = models.LOB.objects.all().annotate(num=Count('faultreport')).values('title', 'num')
    tab_list = models.Tag.objects.all().annotate(num=Count('faultreport')).values('title', 'num')

    # 日期归档的数据
    archive_list = models.FaultReport.objects.all().extra(
        # select = {'ym': 'strftime("%%Y-%%m", create_time, )'}, # sqilite3 语法
        # mysql语法 日期格式化
        select={'ym': 'date_format(create_time, "%%Y-%%m")'},
    ).values('ym').annotate(num=Count('id')).values('ym', 'num')

    report_list = models.FaultReport.objects.all()

    # 二级路由处理
    if args and len(args) == 2:
        if args[0] == 'lob':
            # 进入细分查询：
            report_list = report_list.filter(lob__title=args[1])
        elif args[0] == 'tag':
            report_list = report_list.filter(tags__title=args[1])
        else:
            try:
                year, month = args[1].split('-')
                report_list = report_list.filter(create_time__year=year, create_time__month=month)
            except Exception:
                report_list = []

    return render(request, 'index.html', locals())


class RegisterView(views.View):

    def get(self, request):
        # 实例化一个form对象
        form_obj = forms.RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        res = {'code': 0}
        # 数据有效性校验
        form_obj = forms.RegisterForm(request.POST)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('re_password')
            # 头像数据单独拿
            avatar_obj = request.FILES.get('avatar')
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            res['code'] = 1
            res['error'] = form_obj.errors

        return JsonResponse(res)


def logout(request):
    auth.logout(request)  # request.session.flush()
    return redirect('/login/')
