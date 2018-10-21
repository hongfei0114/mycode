from django.template import Library
from django.conf import settings
import copy
from django.utils.safestring import mark_safe
import re

# （特殊要求）在此处定义函数

register = Library()


@register.simple_tag  # 显示简单的字符串，不适宜模板语言
def show_menu(a1):
    # return "666"
    return mark_safe("<a>菜单1</a>")  # mark_safe可以安全的显示标签


@register.inclusion_tag('menu.html')
def get_menu(request):
    """
    :param request: 请求相关的所有数据
    :return:
    """
    new_menu_list = copy.deepcopy(settings.MEAU_LIST)
    flag = False
    for item in new_menu_list:
        for child in item['children']:
            reg = '^{0}$'.format(child['url'])  # ^/web/edit_user/(\d+)/$
            # if request.path_info == child['url']:  # 编辑的时候有正则匹配，需要更改这里
            if re.match(reg, request.path_info):
                if child['is_menu']:
                    child['class'] = 'active'
                else:
                    index = child['parent_index']
                    item['children'][index]['class'] = 'active'
                item['class'] = ''  # 把当前选中的二级菜单的父菜单的默认收缩hide去掉
                flag = True
                break
        if flag:
            break
    return {'obj': new_menu_list}
