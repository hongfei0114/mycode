import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto.settings")

    permission_list = [
        {
            'permissions__title': '用户列表',
            'permissions__url': '/app01/user/',
            'permissions__name': 'user_list',
            'permissions__menu_id': 1,
            'permissions__menu__title': '用户管理',
            'permissions__menu__icon': 'fa-clipboard',
            'permissions__parent_id': None,
            'permissions__parent__name': None
        },
        {
            'permissions__title': '订单列表',
            'permissions__url': '/app01/order/',
            'permissions__name': 'order',
            'permissions__menu_id': 2,
            'permissions__menu__title': '商品管理',
            'permissions__menu__icon': 'fa-clipboard',
            'permissions__parent_id': None,
            'permissions__parent__name': None
        }
    ]

    menu_dict = {}
    for item in permission_list:
        menu_dic = {}
        menu_id = item['permissions__menu_id']
        if menu_id in menu_dict:
            pass
        else:
            title = item.get('permissions__menu__title')
            icon = item.get('permissions__menu__icon')
            children = [
                {
                    'title': item['permissions__title'],
                    'url': item['permissions__url']
                }
            ]
        menu_dic = {'title': title, 'icon': icon, 'children': children}
        menu_dict[menu_id] = menu_dic
    print(menu_dict)
