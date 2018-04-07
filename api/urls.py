from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('api.users.urls', namespace='users')),
    path('partys/', include('api.partys.urls', namespace='partys')),
]
