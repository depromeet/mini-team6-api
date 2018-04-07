from django.urls import path

from .views import PartyView

app_name = 'partys'
urlpatterns = [
    path('party', PartyView.as_view(), name='PartyView'),
]
