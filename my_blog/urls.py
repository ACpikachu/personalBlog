'''
Date: 2021-10-31 16:49:59
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 16:47:15
FilePath            : /my_blog/my_blog/urls.py
'''



"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
    
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    
    path('password-reset/', include('password_reset.urls')),
    
    path('comment/', include('comment.urls', namespace='comment')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
