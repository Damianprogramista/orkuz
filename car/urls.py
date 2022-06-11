from rest_framework.routers import DefaultRouter

from .views import CarViewSet

app_name = "car"

router = DefaultRouter()

router.register("", CarViewSet)

urlpatterns = router.urls
