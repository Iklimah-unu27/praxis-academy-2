from django.db import models

class Pegawai(models.Model):
    nama = models.CharField( max_length=255)
    telp = models.IntegerField(default='')
    alamat = models.TextField(default='')
