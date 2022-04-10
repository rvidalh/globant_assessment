import requests
import beaufort_scale

from datetime import datetime

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils import timezone

from apps.weather.utils.open_weather_integrator import OpenWeatherIntegrator
from apps.weather.helpers.temp_converter import TempConverter
from apps.weather.helpers.wind_descriptor import WindDescriptor


class WeatherInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(60*2))
    def get(self, request, city=str, country=str):

        if len(country) > 2:
            return Response({'result': 'The country code must be 2 character long.'}, status=status.HTTP_400_BAD_REQUEST)

        open_weather_integrator = OpenWeatherIntegrator()
        content, api_status = open_weather_integrator.get_open_weather_data(city=city, country=country.lower())
        headers = { 'content-type': 'application/json', }

        if api_status != 200:
            return Response({'result': content}, status=api_status)

        temps_helper= TempConverter()
        wind_descriptor = WindDescriptor()

        # get data collection by key
        main = content['main']
        wind = content['wind']
        sys = content['sys']
        coord = content['coord']

        # output data
        city_name = content['name']
        country_code = sys['country']
        kelvin_temp = main['temp']
        celsius = temps_helper.kelvin_to_celsius(kelvin_temp)
        fahrenheit = temps_helper.kelvin_to_fahrenheit(kelvin_temp)
        wind_speed = wind['speed']
        # user a github reference to get wind direction descriptor https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f
        wind_direction = wind_descriptor.wind_direction(wind['deg'])
        # use a library to get beaufort scale to describe wind persuation.
        wind_spedd_beaufort_scale = beaufort_scale.beaufort_scale_ms(wind['speed'], language='en')
        cloud_description = content['weather'][0]['description']
        pressure = main['pressure']
        humidity = main['humidity']
        sunrise_time = datetime.fromtimestamp(sys['sunrise'], tz=timezone.utc).strftime('%H:%M')
        sunset_time = datetime.fromtimestamp(sys['sunset'], tz=timezone.utc).strftime('%H:%M')
        requested_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        # forecast fields
        feels_like_celsius = temps_helper.kelvin_to_celsius(main['feels_like'])
        feels_like_fahrenheit = temps_helper.kelvin_to_fahrenheit(main['feels_like'])

        min_temp_celsius = temps_helper.kelvin_to_celsius(main['temp_min'])
        min_temp_fahrenheit = temps_helper.kelvin_to_fahrenheit(main['temp_min'])

        max_temp_celsius = temps_helper.kelvin_to_celsius(main['temp_max'])
        max_temp_fahrenheit = temps_helper.kelvin_to_fahrenheit(main['temp_max'])

        response_json = {
            "location_name": f'{city_name}, {country_code}',
            "temperature": f'{str(celsius)}°C/{str(fahrenheit)}°F',
            "wind": f'{wind_spedd_beaufort_scale}, {wind_speed} m/s, {wind_direction}',
            "cloudiness": cloud_description,
            "pressure": f'{pressure} hpa',
            "humidity": f'{humidity}%',
            "sunrise": f'{sunrise_time} GTM',
            "sunset": f'{sunset_time} GTM',
            "geo_coordinates": str([coord['lon'], coord['lat']]),
            "requested_time": f'{requested_time} GTM',
            "forecast": {
                "feels_like": f'{feels_like_celsius}°C/{feels_like_fahrenheit}°F',
                "minimum_temperature": f'{min_temp_celsius}°C/{min_temp_fahrenheit}°F',
                "maximum_temperature": f'{max_temp_celsius}°C/{max_temp_fahrenheit}°F',
            },
        }
        return Response(response_json, status=api_status, headers=headers)
