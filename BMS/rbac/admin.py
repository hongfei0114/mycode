from django.contrib import admin
from rbac import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Role)


# 自定义一个权限的管理类
class PermissionAdmin(admin.ModelAdmin):
    # 告诉Django admin在页面上展示我这张表的哪些字段
    list_display = ["title", "url", "is_menu", "icon"]
    # 在列表页面支持直接修改的字段
    list_editable = ["url", "is_menu", "icon"]


admin.site.register(models.Permission, PermissionAdmin)
