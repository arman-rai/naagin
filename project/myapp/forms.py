from django import forms

from .models import Reservatoion

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservatoion
        fields = '__all__'
        