from django.urls import path

from . import views

app_name = 'mobile'

urlpatterns = [
    path('list/', views.MobileListView.as_view(), name='mobiles_list'),
    path('create/', views.MobileCreateView.as_view(), name='mobile_create'),
]
