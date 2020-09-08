from django.forms import ModelForm

from . import models

class MhsForm(ModelForm):
    class Meta :
        model = models.Mhs
        exclude=[]