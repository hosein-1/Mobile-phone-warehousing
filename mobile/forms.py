from django import forms

from .models import Mobile, Brand

class MobileCreateForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'status', 'country_of_origin']


class BrandCreateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']