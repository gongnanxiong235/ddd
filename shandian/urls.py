"""myset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from shandian import views

urlpatterns = [
    # re_path(r'database/([0-9 a-z A-Z]*)/',views.database),
    # re_path(r'sms/([0-9]*)/',views.sms),
    # re_path(r'old2new/([0-9]*)/',views.old2new),
    path('index/',views.index),
    path('database/',views.database),
    path('sendsms/', views.sendSms),
    path('old2new',views.old2new),
    path('setlevel',views.setWXUsertLevel),
    path('old2new_mobile',views.old2new_mobile)
]
