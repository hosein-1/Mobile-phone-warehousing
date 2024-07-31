from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Mobile(models.Model):
    MOBILE_STATUS_AVAILABLE = 'available'
    MOBILE_STATUS_UNAVAILABLE = 'unavailable'
    
    MOBILE_STATUS = [
        (MOBILE_STATUS_AVAILABLE, 'موجود'),
        (MOBILE_STATUS_UNAVAILABLE, 'ناموجود')
    ]
    brand = models.ForeignKey( Brand,
                              on_delete=models.CASCADE,
                              related_name='mobiles',
                              verbose_name='برند')
    
    model = models.CharField(max_length=255, unique=True, verbose_name='مدل')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    color = models.CharField(max_length=50, verbose_name='رنگ')
    screen_size = models.PositiveIntegerField(verbose_name='سایز صفحه نمایش')
    status = models.CharField(max_length=11,
                              choices=MOBILE_STATUS,
                              default=MOBILE_STATUS_AVAILABLE,
                              verbose_name='موجودی')
    country_of_origin = models.CharField(max_length=50, verbose_name='کشور سازنده')
    
    def __str__(self) -> str:
        return f'{self.brand}: {self.model}'
