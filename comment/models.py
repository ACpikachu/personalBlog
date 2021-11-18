'''
Date                : 2021-11-17 19:54:10
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 19:55:12
FilePath            : /my_blog/comment/models.py
'''
from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
from ckeditor.fields import RichTextField

# 博文的评论
class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    # body = models.TextField() 修改为富文本
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]