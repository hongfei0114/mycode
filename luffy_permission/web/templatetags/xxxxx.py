
# 在此处定义函数（特殊要求）

from django.template import Library

register = Library()

@register.simple_tag()
def show_menu():
    return 666
