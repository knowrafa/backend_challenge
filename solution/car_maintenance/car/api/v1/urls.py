from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('cars', views.CarViewSet, basename="car")

car_router = routers.NestedSimpleRouter(router, 'cars', lookup='car')
# car_router.register('tyres', views.TyreViewSet, basename='tyre')

urlpatterns = [
    path("", include(router.urls)),
    path("car_router", include(car_router.urls)),
]
