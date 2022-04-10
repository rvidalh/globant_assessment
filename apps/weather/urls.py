from django.urls import re_path, path
from apps.weather import views


urlpatterns = [
    re_path(r'^weather/(?P<city>[a-zA-Z]+)/(?P<country>[a-zA-Z]+)/$', views.WeatherInfo.as_view(), name='weather'),
]