from time import sleep

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from rest_framework.viewsets import ModelViewSet

from car.models import Car
from .serializers import CarSerializer


@method_decorator(cache_control(private=True, max_age=60), name='dispatch')
class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = []
    serializer_class = CarSerializer
