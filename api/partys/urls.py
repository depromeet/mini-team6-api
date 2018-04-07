from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PartyViewSet,GetParty

router = DefaultRouter()
router.register('', PartyViewSet)

app_name = 'partys'
urlpatterns = router.urls
urlpatterns += path('<int:pk>/', GetParty.as_view()),




