from django.db import models
from datetime import datetime

class Pinjam(models.Model):
    nama = models.CharField(max_length=200)
    nim = models.TextField(default='')
    judulbuku = models.TextField(default='')
    tgl_masuk = models.DateField(default=datetime.now)
    

