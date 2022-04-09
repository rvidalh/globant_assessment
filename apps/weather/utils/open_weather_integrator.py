import requests
from django.conf import settings


class OpenWeatherIntegrator:
    def __init__(self):
        super(OpenWeatherIntegrator, self).__init__()
    
    def _call_get_api(self, url:str):
        content = ''
        result = requests.get(
            url,
            timeout=60,
        )
        if result.status_code in [200, 400, 403, 404, 500]:
            try:
                content = result.json()
            except AttributeError:
                content = result.content
        else:
            raise Exception(f'Error al consumir OpenWeatherApi: {result.content}')
        return content, result.status_code
    
    def get_open_weather_data(self, city=str, country=str):
        
        api_key = settings.API_WEATHER_API_KEY
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        url += f'q={city},{country}&appid={api_key}'
        content, status = self._call_get_api(url)
        return content, status

