from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from .models import WeatherData, WeatherURL
from .serializers import WeatherDataSerializer, WeatherURLSerializer
from .utils import fetch_weather_data

class WeatherURLCreate(generics.CreateAPIView):
    queryset = WeatherURL.objects.all()
    serializer_class = WeatherURLSerializer

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')
        if url:
            weather_data = fetch_weather_data(url)
            weather_url = WeatherURL.objects.create(url=url)
            for data in weather_data:
                data['weather_url'] = weather_url
                WeatherData.objects.create(**data)
            # Redirect to WeatherDataList view
            return redirect('weather-data-list', weather_url_id=weather_url.id)
        return Response({"error": "URL is required"}, status=400)

class WeatherDataList(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        weather_url_id = self.kwargs['weather_url_id']
        return WeatherData.objects.filter(weather_url_id=weather_url_id)
