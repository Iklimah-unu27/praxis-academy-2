from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.mahasiswa),
    path('staf/', views.staf),
    path('dosen/', views.dosen),
    
]
