'''
Date                : 2021-11-15 21:16:38
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 17:58:36
FilePath            : /my_blog/article/models.py
'''
from django.db import models
#导入内置user模型
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from django.urls import reverse
from PIL import Image
# Create your models here.

class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    #创建时间
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title




class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) 
    total_views = models.PositiveIntegerField(default=0)
    #栏目外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
        # 保存时处理图片
    def save(self, *args, **kwargs):
        # 调用原有的 save() 的功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article
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