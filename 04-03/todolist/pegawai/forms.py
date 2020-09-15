from django.forms import ModelForm

from . import models

class PegawaiForm(ModelForm):
    class Meta :
        model = models.Pegawai
        exclude=[]