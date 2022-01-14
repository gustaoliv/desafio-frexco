from rest_framework import viewsets
from . import models
from . import serializers


class RegionViewset(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class FruitViewset(viewsets.ModelViewSet):
    queryset = models.Fruit.objects.all()
    serializer_class = serializers.FruitSerializer