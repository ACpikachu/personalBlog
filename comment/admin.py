'''
Date                : 2021-11-17 20:01:10
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 20:01:10
FilePath            : /my_blog/comment/admin.py
'''
from django.contrib import admin
from .models import Comment
# Register your models here.
admin.site.register(Comment)