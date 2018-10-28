from django.db import models


# Create your models here.

# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=16, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

    # roles = models.ManyToManyField(to='Role', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name



# 权限表
class Order(models.Model):
    title = models.CharField(max_length=16, verbose_name='订单表')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
