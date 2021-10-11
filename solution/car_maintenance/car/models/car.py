from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from utils.mixins.models import TimeManagerMixin
from utils.validators import PorcentagemValidator
from utils.validators import MinGasCountValidator, MaxGasCountValidator


class CarModel(TimeManagerMixin):
    ACCEPTED_FOR_REFUEL = 5  # 5% of gas

    CONSUME_BY_LITER = 8.0  # 8km per litre

    name = models.CharField(max_length=50)
    gas_capacity = models.FloatField()
    gas_count = models.FloatField(
        validators=[MinGasCountValidator(0), MaxGasCountValidator(100)], default=100
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
                self.get_total_in_use_tyres < 4,
                self.gas_count == 0,
            ]
        )

    @property
    def can_refuel(self):
        return self.gas_count < self.ACCEPTED_FOR_REFUEL

    @property
    def get_total_in_use_tyres(self):
        return self.tyres.filter(in_use=True).count()
