'''
Date                : 2021-11-16 21:03:38
LastEditors         : 王少帅
LastEditTime        : 2021-11-16 21:03:38
FilePath            : /my_blog/article/admin.py
'''
from django.contrib import admin
from .models import ArticleColumn, ArticlePost
# Register your models here.

admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)