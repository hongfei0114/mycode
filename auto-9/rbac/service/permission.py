from django.conf import settings


def init_permission(user, request):
    """
    用户初始化，将权限信息和菜单信息放入session中
    :param user: 当前登录的用户对象
    :param request: 请求相关的所有数据
    :return:
    """
    permission_menu_list = user.roles.filter(permissions_innull=False).distinct().values(
        'permissions__url',
        'permissions__title',
        'permissions__name',
        'permissions__menu_id',
        'permissions__menu_title',
        'permissions__menu_icon',
        'permissions__parent_id',  # 父权限相关
        'permissions__parent_name ',
    )

    permission_dict = {}
    menu_dict = {}

    # 获取当前用户拥有的所有权限信息
    for item in permission_menu_list:

        # 添加到权限字典中
        name = item['permissions__name']
        url = item['permissions__url']
        menu_id = item['permissions__menu_id']
        parent_name = item['permissions__parent_name']
        permission_dict[name] = {'url': url, 'menu_id': menu_id, 'parent_name': parent_name}

        # 添加到菜单字典中
        if menu_id:
            menu_id = item['permissions__menu_id']
            if menu_id in menu_id:
                menu_dict[menu_id]['children'].append(
                    {
                        'title': item['permissions__menu_title'],
                        'url': item['permissions__url'],
                        'name': item['permissions__name'],
                    }
                )

            else:
                menu_dict[menu_id] = {
                    'title': item['permissions__title'],
                    'icon': item['permissions__menu_icon'],
                    'children': [
                        {
                            'title': item['permissions__menu_title'],
                            'url': item['permissions__url'],
                            'name': item['permissions__name'],
                        }
                    ]

                }

    request.session[settings.RBAC_PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.RBAC_MENU_SESSION_KEY] = menu_dict
