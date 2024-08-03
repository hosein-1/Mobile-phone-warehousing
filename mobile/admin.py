from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


from .models import Brand, Mobile

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')


@admin.register(Mobile)
class mobileModelAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'price',
        'color',
        'screen_size',
        'status',
        'country_of_origin',
        'datetime_created',
    )