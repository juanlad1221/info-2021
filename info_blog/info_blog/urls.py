"""info_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib.auth import login
#from django.contrib.auth.views import logout_then_login
from django.urls import path
from login import views
from post import views as postViews
from comments import views as commentViews


urlpatterns = [
    #Login y admin
    path('admin', admin.site.urls, name='admin'),
    path('login', views.showLogin, name='login'),
    path('authenticate', views.autenticate, name='authenticate'),
    path('logout', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    #posts
    path('allpost', postViews.allPost, name = 'allpost'),
    #comments
    path('formComment', commentViews.showFormComments, name = 'showFormComments'),
    path('saveComment/<id>', commentViews.saveComent, name = 'saveComment')

]
