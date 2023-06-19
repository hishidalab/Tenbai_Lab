from django.shortcuts import render
from .models import User, ImageUpload
from .forms import ImageUploadForm, UserForm, LoginForm, CommentForm
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


# def productRegistraView(request):
#     print(request.method)
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST)
#         context = {
#             'form': form,
#         }
#         if form.is_valid():  # フォームの値が正しい時
#             imgup = ImageUpload()
#             # 'name','mainimg','img1','img2','img3',''
#             imgup.name = request.POST['name']
#             imgup.mainimg = request.POST['mainimg']
#             imgup.img1 = request.POST['img1']
#             imgup.img2 = request.POST['img2']
#             imgup.img3 = request.POST['img3']
#             imgup.user = request.user
#             imgup.save()
#             return render('pengin/test.html')
#     else:
#         form = ImageUploadForm()
#         context = {
#             'form': form,
#         }
            
#     return render(request, 'pengin/product_registra.html', context)

# class productRegistraView(CreateView):
#     template_name = "pengin/product_registra.html"
#     form_class = ImageUploadForm

#     def post(self, request):
#         if request.method == 'POST':
#             form = ImageUploadForm(request.POST)
#             if form.is_valid():
#                 form = form.save(commit=False)
#                 form.user = request.user
#                 form.save()
#                 return render(request, 'pengin/test.html')
#             else:
#                 return HttpResponse("フォームが無効です。")  # 無効なフォームの場合の処理
#         else:
#             return HttpResponse("無効なリクエストメソッドです。")  # POST 以外のリクエストメソッドの場合の処理

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
            return redirect('test')  # 保存成功後にリダイレクトするURLを指定してください
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
    return render(request, template_name, context)

def BuyFormView(request):
    template_name = "pengin/buy_form.html"
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    context = {
        'users': sample_users,
        'images': img_list,
    }
    print(sample_users)

    return render(request, template_name, context)


# def display_comments(request, thread_id):
#     #該当する掲示板一件を取得
#     threads = Thread.objects.filter(pk=thread_id).values()
#     thread  = threads[0]
#     username_dicts = User.objects.filter(pk=threads[0]['user_id']).values('username')
#     thread.update(username_dicts[0])
#     #該当する掲示板に紐づくコメントを取得
#     comments = Comment.objects.filter(thread_id=thread_id).values()
#     count = len(comments)
#     #コメントのユーザーIDからユーザー名を取得してオブジェクトに追加
#     for count in range(count):
#         username_dicts = User.objects.filter(pk=comments[count]['user_id']).values('username')
#         comments[count].update(username_dicts[0])
#     #フォーム作成
#     form = CommentForm()
#     context = {
#         'thread': thread,
#         'comments': comments,
#         'form': form,
#     }
#     return render(request, 'pengin/buy_form.html', context)

def messageView(request):
    template_name = "pengin/buy_form.html"

    #フォーム作成
    form = CommentForm
    context = {
        'form': form,
    }
    return render(request, template_name, {'form': form})