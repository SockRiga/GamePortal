from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('guides', views.guides, name='guides'),
    path('post1', views.post1, name='post1'),
    path('post2', views.post2, name='post2'),
    path('post3', views.post3, name='post3'),
    path('guid1', views.guid1, name='guid1'),
    path('guid2', views.guid2, name='guid2'),
]