from django.db import models

class Task(models.Model):
    penulis = models.TextField(default='')
    judul = models.TextField(default='')
   

