from django.shortcuts import render
from .models import User, ImageUpload
from .forms import ImageUploadForm, UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views import View

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

            return render(request, 'pengin/signup_check.html', {})
    
    else: #初回アクセス時…空のフォームがほしいとき

        form = UserForm()

    return render(request, 'pengin/signup.html', {"user_form": form})

def loginDataView(request):
    print('request.method == POST')
    print(request.method)
    # ↑GET
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            print('成功')
            user = form.get_user()
            if user:
                login(request, user)
            return render(request, 'pengin/test.html', {})
        else:
            print('そんな値はないです')
            for ele in form :
                print(ele)
    else:
        form = LoginForm()

    return render(request, 'pengin/login.html', {'form': form})

def signupCheckView(request):
    return render(request, 'pengin/signup_check.html')


class ImageUploadView(View):
    template_name = 'pengin/product_registra.html'

    def get(self, request):
        form = ImageUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save(commit=False)
            image_upload.user = request.user
            image_upload.save()
            return redirect('pengin/listing_complete')
        return render(request, self.template_name, {'form': form})
    
def HomeListView(request):
    template_name = "pengin/home.html"
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    context = {
        'users': sample_users,
        'images': img_list,
    }
    print(sample_users)

    print(request.method)
    if request.method == 'POST':
        for img in img_list:
            name = img.get('name')
            nowID = img.get('id')
            print(name)
            if name in request.POST:
                print('ボタン押されたで')
                print(nowID)
                # return render()
        
        

    return render(request, template_name, context)

def ListingCompleteView(request):
    template_name = "pengin/listing_complete.html"
    return render(request,template_name)