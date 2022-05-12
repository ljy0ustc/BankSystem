"""BankSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django import views
from django.contrib import admin
from django.urls import path
from app0 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',views.login),
    path('index/',views.index),
    path('index/client/',views.client),
    path('index/client/detail',views.client_detail),
    path('index/client/new',views.client_new),
    path('index/client/edit',views.client_edit),
    path('index/account/',views.account),
    path('index/account/detail',views.account_detail),
    path('index/account/cheque_new',views.cheque_account_new),
    path('index/account/saving_new',views.saving_account_new),
    path('index/account/edit',views.account_edit),
    path('index/loan/',views.loan),
    path('index/loan/pay',views.pay_loan),
    path('index/loan/new',views.loan_new),
    path('index/business/',views.business),
]
