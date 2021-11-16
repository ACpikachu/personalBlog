'''
Date                : 2021-11-15 21:16:38
LastEditors         : 王少帅
LastEditTime        : 2021-11-15 22:26:27
FilePath            : /my_blog/article/models.py
'''
from django.db import models
#导入内置user模型
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    total_views = models.PositiveIntegerField(default=0)
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
    # ordering 指定模型返回的数据的排列顺序
    # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
    
    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])    