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

    path('product_registra/pengin/listing_complete',ListingCompleteView,name='listing_complete'),
]