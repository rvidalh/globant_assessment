
class TempConverter:
    def __init__(self):
        super(TempConverter, self).__init__()
    
    def kelvin_to_celsius(self, kelvin):
        return round(kelvin - 273.15, 0)
    
    def kelvin_to_fahrenheit(self, kelvin):
        return round((kelvin * (9/5)) - 459.67, 0)