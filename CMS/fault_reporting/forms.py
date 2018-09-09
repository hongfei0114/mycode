import re
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from fault_reporting import models


def check_emaik(value):
    ret = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', value)
    if not ret:
        raise ValidationError('邮箱格式不正确')
    return value


# 注册的form类
class RegisterForm(forms.Form):
    username = forms.CharField(min_length=2, label='用户名')
    password = forms.CharField(
        label='密码',
        min_length=6,
        widget=forms.widgets.PasswordInput()
    )
    re_password = forms.CharField(
        label='确认密码',
        min_length=6,
        widget=forms.widgets.PasswordInput()
    )
    phone = forms.CharField(
        label='手机号',
        min_length=11,
        max_length=11,
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式不正确')],
    )
    email = forms.CharField(
        label='邮箱',
        validators=[check_emaik]
    )

    # 做用户名不能重复的校验
    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            raise ValidationError('用户名已被注册')
        return username

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')

        if re_pwd != pwd:
            # 两次天填写的密码不一致
            self.add_error('re_password', '两次密码不一致')  # 添加错误给字段
            raise ValidationError('两次密码不一致')
        return self.cleaned_data



    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 循环给每个字段加一个类
        for fieid in iter(self.fields):
            self.fields[fieid].widget.attrs.update({
                'class': 'form-control'
            })
