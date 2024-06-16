from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import WeatherURL, WeatherData
from .utils import fetch_weather_data

class WeatherURLCreateTests(APITestCase):
    def test_create_weather_url(self):
        url = reverse('weather-url-create')
        data = {'url': 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Scotland.txt'}
        response = self.client.post(url, data, format='json')
        
        # Check for redirect response
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        # Follow the redirect
        redirect_url = response['Location']
        follow_response = self.client.get(redirect_url)
        self.assertEqual(follow_response.status_code, status.HTTP_200_OK)
        
        # Check data creation
        self.assertEqual(WeatherURL.objects.count(), 1)
        self.assertEqual(WeatherData.objects.count(), len(fetch_weather_data('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Scotland.txt')))


class WeatherDataListTests(APITestCase):
    def setUp(self):
        self.weather_url = WeatherURL.objects.create(url='https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Scotland.txt')
        weather_data = fetch_weather_data('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Scotland.txt')
        for data in weather_data:
            data['weather_url'] = self.weather_url
            WeatherData.objects.create(**data)

    def test_list_weather_data(self):
        url = reverse('weather-data-list', kwargs={'weather_url_id': self.weather_url.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), WeatherData.objects.filter(weather_url=self.weather_url).count())
