from django.urls import path

from . import views

app_name = 'mobile'

urlpatterns = [
    path('create/', views.MobileCreateView.as_view(), name='mobile_create'),
    path('brands/list', views.BrandListView.as_view(), name='brands_list'),
    path('brand/create/', views.BrandCreateView.as_view(), name='brand_create'),
]
