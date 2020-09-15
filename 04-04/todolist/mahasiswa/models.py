from django.db import models

class Mhs(models.Model):
    nama = models.CharField( max_length=255)
    nim = models.CharField( max_length=100)
    status = models.CharField( max_length=100)
    telp = models.IntegerField(default=0)
    alamat = models.TextField(default='')
