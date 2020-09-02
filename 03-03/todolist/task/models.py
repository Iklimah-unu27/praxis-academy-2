from django.db import models

class Task(models.Model):
    penulis = models.TextField(default='')
    judul = models.TextField(default='')
    pnb = models.TextField(default='')
    isbn = models.IntegerField(default=0)
    desc = models.TextField(default='')


