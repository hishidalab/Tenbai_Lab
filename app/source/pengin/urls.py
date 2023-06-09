from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.views import View

app_name = "pengin"
urlpatterns = [
    path("test/", testView, name='test'),
    path('signup/', signupDetaView, name='signup'),
    path('login/', loginDataView, name='login'),
    path('signup_check/', signupCheckView, name='signup_check'),
    path("product_registra/", ImageUploadView.as_view(), name='product_registra'),
    path('home/',HomeListView,name='home'),
    path('buyaddform/<int:number>/',BuyFormAddView,name='buyaddform'),
    path('buy_form/',messageView,name='buy_form'),
    path('product_registra/pengin/listing_complete',ListingCompleteView,name='listing_complete'),
    path('mypage/', mypageView, name='mypage'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('derete_check/', derete_check, name='derete_check'),
    path('search/', searchDateView, name='search'),
]