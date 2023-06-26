from django.shortcuts import render
from .models import User, ImageUpload, Comment
from .forms import ImageUploadForm, UserForm, LoginForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

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
            return render(request, 'pengin/home.html', {})
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
    result_url = "pengin/buy_form/"
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    context = {
        'users': sample_users,
        'images': img_list,
    }
    # print(sample_users)
    # print(request.method)
    if request.method == 'POST':
        for img in img_list:
            name = img.get('name')
            nowID = img.get('id')
            # print(name)
            if name in request.POST:
                print('ボタン押されたで')
                print(type(nowID))
                # return render()
                # result = f"/pengin/buy_form/{nowID}"
                # return redirect(result)
                # url = reverse('BuyFormView', kwargs={'number': nowID})
                # return HttpResponseRedirect(url)
    return render(request, template_name, context)

def ListingCompleteView(request):
    template_name = "pengin/listing_complete.html"
    return render(request,template_name)

def BuyFormView(request):
    template_name = "pengin:buy_form"
    form = CommentForm
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    context = {
        'form':form,
        'users': sample_users,
        'images': img_list,
    }
    print(sample_users)

    return render(request, template_name, context)

def BuyFormAddView(request, number):
    template_name = "pengin/buy_form.html"
    form = CommentForm
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    comment = Comment.objects.values('comment', 'user', 'thread')
    user = User.objects.values('id', 'name', 'loginID', 'createDate', 'active', 'staff', 'admin')
    # print("~~~~~~~~~~~")
    # print(comment)
    # print("--")
    # print(user)
    # print("~~~~~~~~~~~")
    context = {
        'number':number,
        'form': form,
        'image': img_list,
        'comment': comment,
        'user': user
    }
    return render(request, template_name, context)

def messageView(request):
    # template_name = "pengin:buy_form"
    template_name = "pengin:buyaddform"
    number = request.POST['number']
    print(number)

    form = CommentForm(data=request.POST)

    # if request.method == "POST":  # フォームの入力を終えてすべてのフォームのデータともにviewに戻るとき
    #     form = UserForm(request.POST)  # ProfileFormを作る（？）

    print(form.is_valid())

    if form.is_valid():  # フォームの値が正しい時
        print('成功')
        comment = form.save(commit=False)
        print(request.user)
        comment.user = request.user
        thread_number = ImageUpload.objects.get(id=number) 
        comment.thread = thread_number
        comment.save()
        print(thread_number)

        return redirect(template_name, number=number)
       
        # return render(request, template_name, context)

    else: #初回アクセス時…空のフォームがほしいとき
        #フォーム作成
        context = {
            'form': form,
        }
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

def mypageView(request):
    sample_users = User.objects.values('id', 'name','loginID')
    img_list = ImageUpload.objects.values('id','name','mainimg','img1','img2','img3','user')
    context = {
        'img_list':img_list,
    }
    
    myuser = request.user
    myuser = str(myuser)
    myuserID = ''
    print('-----------------------')
    for user in sample_users:
        print(type(user.get('loginID')))
        print(user.get('loginID'))
        print(type(myuser))
        print(myuser)
        if user.get('loginID') == myuser:
            print('-------if----------------')
    #         print(user.get('id'))
    #         print('-----------------------')
            myuserID=user.get('id')
            context['ID'] = myuserID
    # for img in img_list:
    #     if img.get('user') == myuserID:
    return render(request, 'pengin/mypage.html',context)

