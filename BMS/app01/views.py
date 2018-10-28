from django.shortcuts import render, HttpResponse, redirect
from rbac.models import UserInfo
from rbac.serives.permission import init_permission
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        user_obj = UserInfo.objects.filter(username=username, password=pwd).first()
        if user_obj:
            # 登录成功
            # 初始化权限信息
            init_permission(request, user_obj)
            return redirect("/book/list/")
        else:
            return HttpResponse("用户名密码错误")

    return render(request, "login.html")


def book_list(request):
    return render(request, "book_list.html")


def add_book(request):
    return render(request, "add_book.html")
