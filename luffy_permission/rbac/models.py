from django.db import models


# Create your models here.

# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=16, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField(to='Role', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name




# 角色
class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name='角色名称')
    # 因为由角色查询对应的角色的场景多 所以把多对多设计到Role表中
    permissions = models.ManyToManyField(to='Permission')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = verbose_name

# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=16, verbose_name='权限名称')
    url = models.CharField(max_length=255, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
