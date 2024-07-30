from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Phone(models.Model):
    MOBILE_STATUS_AVAILABLE = 'available'
    MOBILE_STATUS_UNAVAILABLE = 'unavailable'
    
    MOBILE_STATUS = [
        (MOBILE_STATUS_AVAILABLE, 'موجود'),
        (MOBILE_STATUS_UNAVAILABLE, 'ناموجود')
    ]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    model = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.PositiveIntegerField()
    status = models.CharField(max_length=11,
                              choices=MOBILE_STATUS,
                              default=MOBILE_STATUS_AVAILABLE)
    country_of_origin = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.brand}: {self.model}'
