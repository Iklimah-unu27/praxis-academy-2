
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('task/', include('task.urls')),
    path('peminjam/', include('peminjam.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
]
