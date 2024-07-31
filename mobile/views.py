from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Mobile, Brand
from .forms import MobileForm

class MobileListView(ListView):
    model = Mobile
    template_name = 'mobile/mobiles_list.html'
    
    
class MobileCreateView(CreateView):
    model = Mobile
    template_name = 'mobile/create_mobile.html'
    form_class = MobileForm
    success_url = reverse_lazy('mobile:mobiles_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
    
