from django.db import models
from datetime import datetime


class Task(models.Model):
    penulis = models.TextField(default='')
    judul = models.TextField(default='')
    pnb = models.TextField(default='')
    isbn = models.IntegerField(default=0)
    desc = models.TextField(default='')


class Pinjam(models.Model):
    nama = models.CharField(max_length=200)
    nim = models.TextField(default='')
    judulbuku = models.TextField(default='')
    tgl_masuk = models.DateField(default=datetime.now)
    

