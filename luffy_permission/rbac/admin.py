from django.contrib import admin
from rbac import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Role)


class PermissionAdmin(admin.ModelAdmin):
    # 告诉django admin 在页面上展示表的哪些字段
    list_display = ["title", "url"]
    # 在页面支持直接修改的字段
    list_editable = ["url", ]


admin.site.register(models.Permission, PermissionAdmin)  # 使用上面的class字段