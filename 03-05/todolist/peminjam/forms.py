from django.forms import ModelForm

from . import models

class PinjamForm(ModelForm):
    class Meta :
        model = models.Pinjam
        exclude=[]