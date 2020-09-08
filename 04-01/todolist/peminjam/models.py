from django.db import models
from datetime import datetime

class Pinjam(models.Model):
    nama = models.CharField(max_length=200)
    nim = models.CharField(max_length=100)
    judulbuku = models.CharField(max_length=200)
    tgl_masuk = models.DateField(default=datetime.now)
    

