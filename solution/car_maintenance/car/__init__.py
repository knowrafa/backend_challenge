from django.apps import AppConfig

default_app_config = 'car.CarConfig'


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car'
