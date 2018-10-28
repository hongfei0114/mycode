from django.db import models


# Create your models here.


class Menu(models.Model):
    """
    菜单表
    """
    title = models.CharField(max_length=32, verbose_name='标题')
    icon = models.CharField(max_length=32, verbose_name='图标')


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(max_length=32, verbose_name='权限名称')
    url = models.CharField(max_length=255, verbose_name='URL')
    name = models.CharField(max_length=32, verbose_name='别名', unique=True)
    menu = models.ForeignKey(to='Menu', verbose_name='管理菜单', null=True, blank=True)
    parent = models.ForeignKey(to='Permission', verbose_name='父菜单', null=True, blank=True)  # 关联当给前表


class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=16, verbose_name='部门')
    permissions = models.ManyToManyField(to='Permission', verbose_name='关联权限')


class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=43, verbose_name='姓名')
    password = models.CharField(max_length=64, verbose_name='密码')
    roles = models.ManyToManyField(to='Role', verbose_name='角色')
