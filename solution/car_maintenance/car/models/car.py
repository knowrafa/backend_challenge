from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from utils.mixins.models import TimeManagerMixin
from utils.validators import PorcentagemValidator


class CarModel(TimeManagerMixin):
    ACCEPTED_FOR_REFUEL = 5  # 5% of gas

    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gas_capacity = models.FloatField()
    gas_count = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=100
    )

    class Meta:
        db_table = "car"
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    @property
    def can_create_in_use_tyre(self):
        return self.tyres.filter(in_use=True).count() < 4

    @property
    def can_start_trip(self):
        return not any(
            [
                self.get_total_active_tyres < 4,
                self.gas_count == 0,
            ]
        )

    @property
    def can_refuel(self):
        return self.gas_count > self.ACCEPTED_FOR_REFUEL

    @property
    def get_total_active_tyres(self):
        return self.tyres.count()
