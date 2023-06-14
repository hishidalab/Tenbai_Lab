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
]