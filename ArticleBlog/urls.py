"""ArticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf.urls.static import static
from .view import *
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/',include("app01.urls")),
    path('index/', index),
    path('about/', about),
    path('listpic/', listpic),
    # path('newslistpic/', newslistpic),
    re_path('newslistpic/(?P<page>\d+)/', newslistpic),
    # path('articleinfo/', articleinfo01),
    re_path("articleinfo/(?P<id>\d*)/",articleinfo),
    path('add_article/', add_article),
    # path('fy_test/', fy_test),
    re_path("fy_test/(?P<page>\d+)/", fy_test),
    path("request_demo/",request_demo),
    path('get_test/',get_test),
    path('post_demo/',post_demo),
    path('getdemo/',get_demo),
    path('postdemo/',post_demo),
    path('register/',register),
    ##ajax路由设置
    path('ajaxdemo/',ajax_demo),
    path('ajax_register/',ajax_register),
    path('ajax_get_req/', ajax_get_req),
    path('ajax_post_req/', ajax_post_req),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ##cookie路由设置
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('delete_cookie/',delete_cookie),
    ###session路由设置
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('delete_session/',delete_session),
    path('login/',login),
    path('logout/',logout),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


