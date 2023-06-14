from django.shortcuts import render
from .models import User, ImageUpload
from .forms import ImageUploadForm, UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def testView(request):
    return render(request, 'pengin/test.html')

def signupDetaView(request):
    template_name = "back/register.html"
    if request.method == "POST":  # フォームの入力を終えてすべてのフォームのデータともにviewに戻るとき
        form = UserForm(request.POST)  # ProfileFormを作る（？）

        if form.is_valid():  # フォームの値が正しい時
            print('成功')
            question = form.save(commit=False)  # フォームを保存 ※commit=Falseでまだ保存しない
            # question.user = request.user
            # question = User(loginID = form.changed_data["loginID"])
            question.set_password(form.cleaned_data["password"])
            question.save()

            return render(request, 'pengin/login.html', {})
    
    else: #初回アクセス時…空のフォームがほしいとき

        form = UserForm()

    return render(request, 'pengin/signup.html', {"user_form": form})

def loginDataView(request):
    print('request.method == POST')
    print(request.method)
    # ↑GET
    if request.method == 'POST':
        # print(LoginForm(request, data=request.POST))
        form = LoginForm(request, data=request.POST)
        print(form)
        # form = LoginForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            print('成功')
            user = form.get_user()
            if user:
                login(request, user)
            return render(request, 'back/home.html', {})
        else:
            print('そんな値はないです')
            for ele in form :
                print(ele)
    else:

        form = LoginForm()

    return render(request, 'pengin/login.html', {'form': form})
