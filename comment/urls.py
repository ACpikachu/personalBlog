'''
Date                : 2021-11-15 22:25:59
LastEditors         : 王少帅
LastEditTime        : 2021-11-15 22:36:51
FilePath            : /my_blog/comment/urls.py
'''
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]