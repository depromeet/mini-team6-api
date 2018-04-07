from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PartyViewSet

router = DefaultRouter()
router.register('', PartyViewSet)

app_name = 'partys'
urlpatterns = router.urls
