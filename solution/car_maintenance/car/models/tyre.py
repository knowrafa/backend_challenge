from django.core.validators import MaxValueValidator

from utils.mixins.models import TimeManagerMixin
from django.db import models


class TyreModel(TimeManagerMixin):
    TYRE_DEGRADATION_FOR_CHANGE = 94  # 94% of degradation

    car = models.ForeignKey('CarModel', related_name='tyres', on_delete=models.CASCADE)
    degradation = models.FloatField(validators=[MaxValueValidator(100)], default=0)
    in_use = models.BooleanField(default=False)

    class Meta:
        db_table = "tyre"
        verbose_name = "Tyre"
        verbose_name_plural = "Tyres"

    @property
    def can_be_swapped(self):
        return self.degradation >= self.TYRE_DEGRADATION_FOR_CHANGE
