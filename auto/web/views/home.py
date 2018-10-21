from django.shortcuts import render, redirect, HttpResponse
from web import models
from django import views
from django.forms import ModelForm


def index(request):
    return render(request, 'index.html')


def user(request):
    user_obj = models.UserInfo.objects.all()
    return render(request, 'user.html', locals())


class UserModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"

        error_messages = {
            'username': {'required': '用户不能为空'}
        }


def add_user(request):
    """
    添加用户
    :return:
    """

    if request.method == 'GET':
        form = UserModelForm()
    else:
        form = UserModelForm(request.POST)
        if form.is_valid():  # 验证非空
            form.save()
            return redirect('/web/user/')

    return render(request, 'add_user.html', locals())


def edit_user(request, uid):
    """
    编辑用户
    :param request:
    :param uid:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=uid).first()  # 拿到用户实例

    if request.method == 'GET':
        form = UserModelForm(instance=obj)  # 在编辑页面展示当前信息
    else:
        form = UserModelForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web/user/')
    return render(request, 'edit_user.html', locals())


def del_user(request, uid):
    """
    删除用户
    :param request:
    :param uid:
    :return:
    """
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect('/web/user/')


def order(request):
    order_obj = models.Order.objects.all()
    return render(request, 'order.html', locals())


class OrderModelForm(ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"

        error_messages = {
            'title': {'required': '名称不能为空'}
        }


def add_order(request):
    if request.method == 'GET':
        form = OrderModelForm()
    else:
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web/order/')
    return render(request, 'add_order.html', locals())


def edit_order(request, uid):
    """
    编辑订单
    :param request: 请求参数
    :param uid: 用户ID
    :return:
    """
    obj = models.Order.objects.filter(id=uid).first()
    if request.method == 'GET':
        form = OrderModelForm(instance=obj)
    else:
        form = OrderModelForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web/order/')

    return render(request, 'edit_order.html', locals())


def del_order(request, uid):
    """
    删除订单
    :param request:
    :param uid:
    :return:
    """
    models.Order.objects.filter(id=uid).delete()
    return redirect('/web/order/')


def center(request):
    return render(request, 'center.html', )
