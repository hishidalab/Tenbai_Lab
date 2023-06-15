from django import forms
from django.db import models
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = {'name','mainimg','img1','img2','img3'}
        labels = {'name':"商品名",'mainimg':"商品メインイメージ",'img1':"サブイメージ1",'img2':"サブイメージ2",'img3':"サブイメージ3"}

class LoginForm(AuthenticationForm):
    fields = {'loginID','password'}
    labels = {'loginID':"ログインID",'password':"パスワード"}

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        print(model)
        # fields = "__all__"
        fields = {'name', 'loginID', 'password'}
        labels = {'username': "ユーザーネーム",
                'loginID': "ログインID", 'password': "パスワード"}
        

# class LoginForm(AuthenticationForm):
#     class Meta:
#         fields = "__all__"