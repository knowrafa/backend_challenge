from django.db import models

from utils.mixins.models import TimeManagerMixin
from utils.validators import MaxDegradationValidator


class TyreModel(TimeManagerMixin):
    TYRE_DEGRADATION_FOR_CHANGE = 94  # % of degradation
    DEGRADATION_BY_KILOMETER = 3  # Degrades 1% per

    car = models.ForeignKey("CarModel", related_name="tyres", on_delete=models.CASCADE)
    degradation = models.FloatField(
        validators=[MaxDegradationValidator(100)], default=0
    )
    in_use = models.BooleanField(default=False)

    class Meta:
        db_table = "tyre"
        verbose_name = "Tyre"
        verbose_name_plural = "Tyres"

    @property
    def can_be_swapped(self):
        return self.degradation >= self.TYRE_DEGRADATION_FOR_CHANGE
