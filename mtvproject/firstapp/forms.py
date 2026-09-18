from django import forms
from .models import Reservetion

class ReservetionForm(forms.ModelForm):
    class Meta:
        model = Reservetion
        fields = ['first_name', 'last_name', 'email',' guess_count', 'reservation_time', 'comments']

