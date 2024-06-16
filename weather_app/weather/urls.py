from django.urls import path
from .views import WeatherURLCreate, WeatherDataList

urlpatterns = [
    path('weather/', WeatherURLCreate.as_view(), name='weather-url-create'),
    path('weather/<int:weather_url_id>/', WeatherDataList.as_view(), name='weather-data-list'),
]
