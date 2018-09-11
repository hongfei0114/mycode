from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
from fault_reporting import forms
from django.http import JsonResponse
from fault_reporting import models
from django.db.models import Count
# django支持事务操作
from django.db import transaction
from django.db.models import F
from django.contrib.auth.decorators import login_required


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


@login_required  # 使用装饰器 需要在settings中指定login的自定义路径
def info(request):
    # 个人中心视图
    report_list = models.FaultReport.objects.filter(user=request.user)  # 如果位登录，会报错。获取不到用户的值。需要判断
    return render(request, 'info.html', locals())


def report_detail(request, report_id):
    # 故障总结详情页
    # 根据id找故障在总结
    report = models.FaultReport.objects.filter(id=report_id).first()
    if not report:
        return HttpResponse('404')
    return render(request, 'report_detail.html', locals())


def updown(request):
    res = {'code': 0}
    user_id = request.POST.get('user_id')
    report_id = request.POST.get('report_id')
    # is_up = request.POST.get('is_up')  # is_up永远是字符串 'true'或者'false'
    is_up = True if request.POST.get("is_up") == 'true' else False
    is_exist = models.UpDown.objects.filter(user_id=user_id, fault_report_id=report_id).first()

    # 1.不能推荐或反对自己的文章
    if models.FaultReport.objects.filter(user_id=user_id, id=report_id):
        # 说明是给自己点赞/反对
        res["code"] = 1
        res["msg"] = "不能支持自己的文章" if is_up else "不能反对自己的文章"
    # 2.每个人只能给一篇文章点一次
    elif is_exist:
        # 如果有记录说明已经点过一次了
        res['code'] = 1
        res["msg"] = "你已经推荐过" if is_exist.is_up else "你已经反对过"

    # 创建点赞记录
    else:
        # 因为点赞表创建的新纪录同事还要更新故障总结表的点赞字段，涉及到事务操作
        with transaction.atomic():
            # 1. 创建点赞记录
            models.UpDown.objects.create(
                user_id=user_id,
                fault_report_id=report_id,
                is_up=is_up,
            )
            # 2. 更新对应故障总结的点赞数
            if is_up:
                models.FaultReport.objects.filter(id=report_id).update(up_count=F('up_count') + 1)

            else:
                models.FaultReport.objects.filter(id=report_id).update(down_cou=inF('down_count') + 1)

        res['msg'] = '推荐成功' if is_up else '反对成功'

    return JsonResponse(res)
