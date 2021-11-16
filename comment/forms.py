'''
Date                : 2021-11-15 22:25:48
LastEditors         : 王少帅
LastEditTime        : 2021-11-15 22:25:48
FilePath            : /my_blog/comment/forms.py
'''
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']