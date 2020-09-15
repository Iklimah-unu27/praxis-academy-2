from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('task/', include('task.urls')),
    path('catatan/', include('catatan.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('pegawai/', include('pegawai.urls')),
    path('profil/', include('profil.urls')),
    path('accounts/',include("accounts.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
