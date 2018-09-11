from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')


class LOB(models.Model):
    """
    line-of-business
    """
    title = models.CharField(max_length=32, unique=True, verbose_name='业务线名称')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    故障标签
    """
    title = models.CharField(max_length=32, verbose_name='标签名称', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class UpDown(models.Model):
    """
    同一个用户只能对一篇故障总结点一次支持或者反对
    """
    user = models.ForeignKey(to='UserInfo', verbose_name='用户')
    fault_report = models.ForeignKey(to='FaultReport', verbose_name='故障总结')
    is_up = models.BooleanField(default=True, verbose_name='支持/反对')

    def __str__(self):
        return "{}-{}-{}".format(self.user.username, self.fault_report, '支持' if self.is_up else '反对')

    class Meta:
        # 用户和故障总结联合唯一
        unique_together = (('fault_report', 'user'),)
        verbose_name = '支持/反对'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论
    """
    fault_report = models.ForeignKey(to='FaultReport', verbose_name='故障总结')
    user = models.ForeignKey(to='UserInfo', verbose_name='用户')
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    # 自己关联自己的内容 父评
    parent_comment = models.ForeignKey(to='self', null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class FaultReport(models.Model):
    """
    故障总结/故障报告
    """
    title = models.CharField(max_length=80, verbose_name='故障标题')
    desc = models.CharField(max_length=255, verbose_name='故障简介')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    lob = models.ForeignKey(to='LOB', null=True, verbose_name='所属产品线')

    comment_count= models.IntegerField(default=0, verbose_name='评论数')
    up_count= models.IntegerField(default=0, verbose_name='点赞数')
    down_count= models.IntegerField(default=0, verbose_name='踩灭数')

    user = models.ForeignKey(to='UserInfo', verbose_name='发布者')
    tags = models.ManyToManyField(
        to='Tag',
        through='Fault2Tag',
        through_fields=('fault_report', 'tag'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '故障总结/故障报告'
        verbose_name_plural = verbose_name


class Fault2Tag(models.Model):
    """
    故障报告和标签的多对多关系表
    """
    fault_report = models.ForeignKey(to='FaultReport')
    tag = models.ForeignKey(to='Tag')

    def __str__(self):
        return "{}-{}".format(self.fault_report, self.tag)

    class Meta:
        unique_together = (('fault_report', 'tag'),)
        verbose_name = '故障-标签'
        verbose_name_plural = verbose_name


class FaultDetail(models.Model):
    """
    故障详情
    """
    content = models.TextField()
    fault = models.OneToOneField(to='FaultReport')

    def __str__(self):
        return self.content[0:50]

    class Meta:
        verbose_name = '故障详情表'
        verbose_name_plural = verbose_name
