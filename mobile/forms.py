from django import forms

from .models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'status', 'country_of_origin']
        