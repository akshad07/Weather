from django.db import models

class WeatherURL(models.Model):
    url = models.URLField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class WeatherData(models.Model):
    weather_url = models.ForeignKey(WeatherURL, related_name='weather_data', on_delete=models.CASCADE)
    year = models.CharField(max_length=20, null=True, blank=True)
    jan = models.CharField(max_length=20, null=True, blank=True)
    feb = models.CharField(max_length=20, null=True, blank=True)
    mar = models.CharField(max_length=20, null=True, blank=True)
    apr = models.CharField(max_length=20, null=True, blank=True)
    may = models.CharField(max_length=20, null=True, blank=True)
    jun = models.CharField(max_length=20, null=True, blank=True)
    jul = models.CharField(max_length=20, null=True, blank=True)
    aug = models.CharField(max_length=20, null=True, blank=True)
    sep = models.CharField(max_length=20, null=True, blank=True)
    oct = models.CharField(max_length=20, null=True, blank=True)
    nov = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    win = models.CharField(max_length=20, null=True, blank=True)
    spr = models.CharField(max_length=20, null=True, blank=True)
    sum = models.CharField(max_length=20, null=True, blank=True)
    aut = models.CharField(max_length=20, null=True, blank=True)
    ann = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Weather Data for {self.year}"
