'''
Author: your name
Date: 2021-11-11 14:44:46
LastEditTime        : 2021-11-17 14:31:49
LastEditors         : 王少帅
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath            : /my_blog/userprofile/urls.py
'''
from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    
    #注册
    path('register/', views.user_register, name='register'),
    
    #删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]