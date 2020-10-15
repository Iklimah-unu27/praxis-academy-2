from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput

from mitra.models import Mitra

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner', 'approve']
        widgets = {
            'tanggal_mulai': DatePickerInput().start_of('event days'),
            'tanggal_selesai': DatePickerInput().end_of('event days'),
        }