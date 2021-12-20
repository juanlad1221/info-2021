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
from django.urls import path
from login import views
from post import views as postViews
from comments import views as commentViews



urlpatterns = [
    #admin django
    path('admin', admin.site.urls, name='admin'),
    #login
    path('login', views.showLogin, name='login'),
    path('authenticate', views.autenticate, name='authenticate'),
    path('logout', views.logout_view, name='logout'),
    #posts
    path('', postViews.allPost, name='home'),
    #comments
    path('formComment', commentViews.showFormComments, name = 'showFormComments'),
    path('saveComment/<id>', commentViews.saveComent, name = 'saveComment'),
    #admin2(propio)
    path('_admin2',views.showAdmin2, name = '_admin2'),
    path('_admin2-post',views.showAdmin2Post, name = '_admin2-post'),
    path('_admin2-post-edit/<id>', views.showAdmin2EditPost, name='_admin2-post-edit'),
    path('_admin2-post-delete/<id>', views.admin2DeletePost , name='_admin2-post-delete'),
    path('_admin2-post-new', views.admin2NewPost, name='_admin2-post-new'),
    path('_admin2-msg', views.admin2Msg, name='_admin2-msg')

]
