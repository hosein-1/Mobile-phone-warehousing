from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Mobile, Brand
from .forms import MobileCreateForm, BrandCreateForm


class MobileListView(ListView):
    model = Mobile
    template_name = 'mobile/mobiles_list.html'
    context_object_name = 'mobiles_queryset'
    paginate_by = 7
    
    

class MobileCreateView(SuccessMessageMixin, CreateView):
    model = Mobile
    template_name = 'mobile/create_mobile.html'
    form_class = MobileCreateForm
    success_url = reverse_lazy('mobiles_list')

    def get_success_message(self, cleaned_data):
        return f'برند <<{self.object.model}>> با موفقیت ذخیره شد.'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context


class BrandListView(ListView):
    model = Brand
    template_name = 'mobile/brands_list.html'
    context_object_name = 'brands_queryset'
    paginate_by = 7


class BrandCreateView(SuccessMessageMixin, CreateView):
    model = Brand
    template_name = 'mobile/create_brand.html'
    form_class = BrandCreateForm
    success_url = reverse_lazy('mobile:brands_list')
    
    def get_success_message(self, cleaned_data):
        return f'برند <<{self.object.name}>> با موفقیت ذخیره شد.'


    
