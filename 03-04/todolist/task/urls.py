
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    ####### CRUD 2 #######
    path('new/', views.new2),
    path('', views.pinjam2),
    path('<id>/', views.detail2),
    path('<id>/delete/', views.delete2),
    path('<id>/update/', views.update2),
]
