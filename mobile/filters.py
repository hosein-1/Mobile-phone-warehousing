import django_filters

from .models import Mobile


class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobile
        fields = ['brand__name', 'brand__nationality','country_of_origin']