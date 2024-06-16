from rest_framework import serializers
from .models import WeatherData, WeatherURL
from rest_framework import serializers
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        exclude = ['id','weather_url']


class WeatherURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True, required=False)

    class Meta:
        model = WeatherURL
        fields = ['url']
