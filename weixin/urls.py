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
from weixin import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('test/',views.test),
    path('time/',views.current_time),
    path('userinfo/',views.userInfo),
    path('temp/',views.template_method),
    path('temp2/',views.template_method_2),
    path('order/',views.order),
    path('li/',views.li),
    path('shopping/',views.shop),
    path('sqlite',views.testsqlite),
    #别名
    path('login/',views.login,name="gongnanxiong"),
    path('alex',views.alex,{"name":"alex"}),
    #正则表达式匹配
    re_path(r'^active/[0-9]{4}/$',views.activite), #不带$表示最后是任意字符都可以匹配到
    re_path(r'^activity/([0-9]{4})/([0-9]{2})',views.activity), #  加小括号表示作为一个参数 映射到的view上的方法中药带此参数
    re_path(r'^group/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})',views.group),

]
