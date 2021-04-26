from rest_framework import routers
from .views import CountryViewSet, StateViewSet, CityViewSet

router = routers.SimpleRouter()
router.register(r'country', CountryViewSet)
router.register(r'city', CityViewSet)
router.register(r'state', StateViewSet)

urlpatterns = router.urls