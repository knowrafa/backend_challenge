from django.db import models

from ..utils.mixins.models import TimeManagerMixin


class CarModel(TimeManagerMixin):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    class Meta:
        db_table = "car"
        verbose_name = "Car"
        verbose_name_plural = "Cars"
