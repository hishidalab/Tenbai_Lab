from django import forms
from django.db import models
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        print(model)
        # fields = "__all__"
        fields = {'name', 'loginID', 'password'}
        labels = {'username': "ユーザーネーム",
                'loginID': "ログインID", 'password': "パスワード"}
        
class LoginForm(AuthenticationForm):
    print("formです")
    fields = {'loginID','password'}
    labels = {'loginID':"ログインID",'password':"パスワード"}