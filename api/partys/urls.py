from django.urls import path

from .views import APIView

app_name = 'partys'
urlpatterns = [
    path('', APIView.as_view(), name='test'),
]
