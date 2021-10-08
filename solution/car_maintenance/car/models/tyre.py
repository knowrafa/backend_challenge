from django.core.validators import MaxValueValidator

from ..utils.mixins.models import TimeManagerMixin
from django.db import models


class TyreModel(TimeManagerMixin):
    car = models.ForeignKey('CarModel', related_name='tyres', on_delete=models.CASCADE)
    degradation = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=100)
    is_active = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        return super(TyreModel, self).save()

    class Meta:
        db_table = "tyre"
        verbose_name = "Tyre"
        verbose_name_plural = "Tyres"
