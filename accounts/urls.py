"""librarymgmt URL Configuration

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
from django.contrib import admin
from django.urls import path
from accounts import views as v

urlpatterns = [
    path('',v.index),

    path('home',v.home,name="home"),

    path('bsearch',v.book_search,name="bsearch"),
    path('booklist',v.booklist,name="booklist"),
    path('addbook',v.add_book,name="addbook"),
    path('editbook/<int:id>',v.edit_book),
    path('bookdetails/<int:id>',v.book_details),
    path('bookissue/<int:id>',v.booksissue),
    #path('bookissue',v.booksissue,name="bookissue"),
    path('booksissued',v.books_issued,name="booksissued"),
    path('deletebook/<int:id>',v.delete_book),
    path('returnbook/<int:id>',v.return_book),


    path('adduserform',v.adduserform,name="adduserform"),
    path('adduser',v.add_user,name="adduser"),
    
    
    path('login',v.login_view,name="login"),
    path('logout',v.logout_view,name="logout"),
]
