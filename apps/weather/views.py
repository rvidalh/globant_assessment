
from operator import truediv
import requests

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.weather.serializers import UserSerializer, GroupSerializer
from apps.weather.utils.open_weather_integrator import OpenWeatherIntegrator


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class WeatherInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, city=str, country=str):
        open_weather_integrator = OpenWeatherIntegrator()
        content, status = open_weather_integrator.get_open_weather_data(city='santiago', country='chile')
        return Response(content, status=status)