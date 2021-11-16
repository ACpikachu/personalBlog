'''
Author: your name
Date: 2021-11-11 11:41:05
LastEditTime: 2021-11-11 20:33:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /my_blog/userprofile/forms.py
'''
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email')
    
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")