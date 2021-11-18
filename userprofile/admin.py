'''
Date                : 2021-11-17 15:50:32
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 15:58:42
FilePath            : /my_blog/userprofile/admin.py
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

from .models import ProFile

class ProfileInline(admin.StackedInline):
    model = ProFile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# 将 Profile 关联到 User 中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
# 重新注册 User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)