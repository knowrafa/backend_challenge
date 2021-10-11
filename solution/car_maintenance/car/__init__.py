from django.apps import AppConfig

default_app_config = 'car.CarConfig'


class CarConfig(AppConfig):
    name = 'car'
    default_auto_field = 'django.db.models.BigAutoField'
