import imp
from api.viewsets import RegionViewset, FruitViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('region', RegionViewset)
router.register('fruit', FruitViewset)
