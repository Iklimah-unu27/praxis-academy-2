from django.db import models

class mahasiswa (models.Model):
    nim = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    sks = models.IntegerField(default='')