'''
Date                : 2021-11-17 17:53:10
LastEditors         : 王少帅
LastEditTime        : 2021-11-17 18:03:17
FilePath            : /my_blog/article/form.py
'''
from django import forms
from .models import ArticlePost

class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'avatar')