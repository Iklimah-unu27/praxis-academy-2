from django.db import models

class Task(models.Model):
    penulis = models.CharField( max_length=255)
    judul = models.CharField( max_length=100)
    pnb = models.CharField( max_length=255)
    isbn = models.IntegerField(default=0)
    desc = models.TextField(default='')
