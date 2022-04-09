from django.urls import re_path
from apps.weather import views

urlpatterns = [
    re_path(r'^weather/(?P<city>[-\w]+)/(?P<country>[-\w]+)/$', views.WeatherInfo.as_view()),
]