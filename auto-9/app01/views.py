from django.shortcuts import render, HttpResponse, redirect
from rbac import models
from rbac.service import permission


def login(request):
    """
    用户登录
    :param request:
    :return:
    用户登录：马帅，UserInfo表中做查询，登录成功后获取两部分数据：
    权限 = {
        "user": {"url":'/app01/user/'},
        "user_add": {"url":'/app01/user/add/'},
        "user_edit": {"url":'/app01/user/edit/(\d+)'},
        "order": {"url":'/app01/order/'},
    }
    
    菜单信息 = {
        1:{
            'title':'用户管理',
            'icon':'fa-clipboard',
            'children':[
                {'title':'用户列表','url':'/app01/user/'},
            ]
        },
        2:{
            'title':'商品管理',
            'icon':'fa-clipboard',
            'children':[
                {'title':'订单列表','url':'/app01/order/'},
            ]
        }
    
    }
    
    
    """
    if request.method == 'GET':
        return render(request, 'app01/login.html', {'msg': '用户名或密码错误'})
    # 1. 取到用户名和密码 进行校验
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user = models.UserInfo.objects.filter(username=user,password=pwd).first()

    if not user:
        return render(request, 'app01/login.html', {'msg': '用户名或密码错误'})
    permission.init_permission(user, request)

    return redirect('/app01/user/')


def user_list(request):

    return HttpResponse('用户列表')


def center(request):
    return HttpResponse('个人中心')
