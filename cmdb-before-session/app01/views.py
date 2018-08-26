from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import views
from app01.handle import md5_encrypt
from utils import mypage


# Create your views here.

# 下面是用户的操作
def login(request):
    '''
    login登录页面，当请求方法是POST的时候 获取用户提交的用户名和密码
    :param request: 
    :return: 返回给用户登录页
    '''

    if request.method == 'POST':
        username = request.POST.get('username', '')
        pwd = md5_encrypt(username, request.POST.get('password', ''))
        obj = models.User.objects.filter(name=username).first()
        if obj:
            if obj.password == pwd:
                return redirect('/user_list/')
    return render(request, 'login.html')


def user_list(request):
    data = models.User.objects.all()
    return render(request, 'user_list.html', {'data': data})


def register(request):
    '''
    注册页面  当用户POST提交的时候，获取用户输入
    判断二次验证一致后，用md5加密存到数据库
    给用户返回user_list页面
    :param request:
    :return:
    '''

    if request.method == 'POST':
        new_user = request.POST.get('username')

        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password == password_confirm:
            password = md5_encrypt(new_user, password)
            models.User.objects.create(name=new_user, password=password)
            return redirect('/user_list/')

    return render(request, 'register.html')


def check_user(request):
    username = request.GET.get('username')
    is_exist = models.User.objects.filter(name=username)
    if not username:
        res = '用户名不能为空'
    elif is_exist:
        res = '用户名已经存在，请直接登录'
    else:
        res = 'OK'
    return HttpResponse(res)


def check_pass(request, ):
    # input_old_pass = request.GET.get('old_pass')
    # user_name = models.User.objects.get(id=reset_id).name
    # user_pass = models.User.objects.get(id=reset_id).password
    # old_pass = md5_encrypt(user_name, input_old_pass)
    password = request.GET.get('password')
    # if not input_old_pass:
    #     res = '密码不正确，请重新输入'
    if not password:
        res = '请输入新密码'
    else:
        res = 'OK'
    return HttpResponse(res)


def check_pass_confirm(request, ):
    password = request.GET.get('password')
    password_confirm = request.GET.get('password_confirm')

    if password != password_confirm:
        res = '密码不一致'
    else:
        res = 'OK'

    return HttpResponse(res)


class DeleteUser(views.View):

    def get(self, request, delid):
        models.User.objects.filter(id=delid).delete()
        return redirect('/user_list/')


class ResetPass(views.View):

    def get(self, request, reset_id):
        user_obj = models.User.objects.filter(id=reset_id)
        return render(request, 'reset_pass.html', {'user': user_obj})

    def post(self, request, reset_id):
        old_pass = request.POST.get("old_pass")
        new_pass = request.POST.get("new_pass")
        pass_confirm = request.POST.get("pass_confirm")

        user_obj = models.User.objects.get(id=reset_id)
        # 验证旧的密码是否成功
        if user_obj.password == md5_encrypt(user_obj.name, old_pass):
            # 验证二次输入
            if new_pass == pass_confirm:
                # ORM层面的变动
                user_obj.password = md5_encrypt(user_obj.name, new_pass)
                # 提交变动到数据库
                user_obj.save()
                # 操作成功 返回user_list
                return redirect('/user_list/')
            else:
                return HttpResponse('密码不一致，请重新输入，还得你自己退回去。http://127.0.0.1:8000/user_list/')
        else:
            return HttpResponse('密码不正确，请自己退回去输入正确的密码：http://127.0.0.1:8000/user_list/')


# 下面是service的操作
class ServiceList(views.View):

    def get(self, request):
        data = models.Service.objects.all()
        return render(request, 'service_list.html', {'data': data, })


class DelService(views.View):

    def get(self, request, service_id):
        models.Service.objects.get(id=service_id).delete()
        return redirect('/service_list/')


class AddService(views.View):

    def get(self, request):
        user = models.User.objects.all()
        return render(request, 'add_service.html', {'user_list': user})

    def post(self, request):
        service_name = request.POST.get('servicename')
        user_id = request.POST.get('user')
        models.Service.objects.create(name=service_name, Users_id=user_id)
        return redirect('/service_list/')


class ConfigService(views.View):

    def get(self, request, service_id):
        service_obj = models.Service.objects.get(id=service_id)
        user = models.User.objects.all()
        hosts = models.Hosts.objects.all()
        return render(request, 'config_service.html',
                      {'service_obj': service_obj, 'user_list': user, 'hosts_list': hosts})

    def post(self, request, service_id):
        service_obj = models.Service.objects.filter(id=service_id).first()
        new_user_id = request.POST.get('user')
        new_hosts = request.POST.getlist("hosts")
        service_obj.Users_id = new_user_id  # 多对一的更改通过id
        service_obj.hosts.set(new_hosts)  # 多对多的更改列表 set
        return redirect('/service_list/')


# 下面是主机的操作
class HostsList(views.View):

    def get(self, request):
        hosts_obj = models.Hosts.objects.all()
        total_count = hosts_obj.count()
        current_page = request.GET.get('page', None)
        page_obj = mypage.MyPage(current_page, total_count, url_prefix='hosts_list', )
        data = hosts_obj[page_obj.start:page_obj.end]
        page_html = page_obj.page_html()
        return render(request, 'hosts_list.html', {'data': data, 'page_html': page_html, })


class DeleteHosts(views.View):

    def get(self, request, delete_id):
        models.Hosts.objects.filter(id=delete_id).delete()
        return redirect('/hosts_list/')


class AddHosts(views.View):

    def get(self, request):
        service_obj = models.Service.objects.all()
        return render(request, 'add_hosts.html', {'service_list': service_obj})

    def post(self, request):
        add_host_name = request.POST.get('hostname')
        add_service = request.POST.getlist("service")
        print(add_host_name, add_service)
        hosts_obj = models.Hosts.objects.create(name=add_host_name)
        hosts_obj.services.set(add_service)

        return redirect('/hosts_list/')


class ConfigHosts(views.View):

    def get(self, request, config_id):
        host_obj = models.Hosts.objects.filter(id=config_id).first()
        service_list = models.Service.objects.all()
        return render(request, 'config_hosts.html', {'host_obj': host_obj, 'service_list': service_list})

    def post(self, request, config_id):
        new_host_name = request.POST.get('hostname')
        add_service = request.POST.getlist("service")
        host_obj = models.Hosts.objects.filter(id=config_id).first()
        host_obj.name = new_host_name
        host_obj.save()  # 不要丢了括号
        host_obj.services.set(add_service)
        return redirect('/hosts_list/')
