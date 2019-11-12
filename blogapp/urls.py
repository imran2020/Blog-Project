"""djangoblock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('author/<name>/',views.getauthor,name="author"),
    path('article/<int:id>/',views.getsingle,name='single_post'),
    path('category/<name>/', views.getcategory, name='category'),
    path('login/', views.getlogin, name='login'),
    path('logout/', views.getlogout, name='logout'),
    path('create/',views.getcreate,name='create'),
    path('profile/',views.getprofile,name='profile'),
    path('update/<int:id>/',views.getupdate,name='update'),
    path('delete/<int:id>/',views.getdelete,name='delete'),
    path('register/',views.getregister,name='register'),
    path('topic/',views.getTopic,name='topic'),
    path('create/category',views.createCategory,name='createCategory'),
    path('activate/<uid>/<token>',views.activate,name='activate'),
    path('chat/',views.chating,name='chat'),
    path('creat_post/',views.create_post,name='create_post'),
    path('myprofile/<int:id>',views.myprofile,name='myprofile'),
    path('edit/<int:id>/',views.edit_post,name='edit'),
    path('get_comment/<int:id>/',views.get_comment,name='get_comment'),
    path('search/',views.search,name='search'),
    path('maintain/',views.maintenence,name='maintain'),
   # path('about/<int:id>',views.user_about,name='about'),


]
