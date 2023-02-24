from unittest import TestCase
from freibadwidget.modules.weather import WeatherModule


class TestCaseBaranquilla(TestCase):

    # Take the Test Location Baranquilla in Colombia
    def setUp(self):
        config = {
            "location":
            {
                    "lat": 10.9727,
                    "lon": -74.7958,
            },
            "open_weather": {
                    "api_key": "cb1d12b9203c27dc4e29250f755ba4d4",
                    "url": "https://api.openweathermap.org/data/2.5/onecall"
            }
        }

        self.weather_module = WeatherModule(config)

    def test_current(self):
        self.weather_module.get_update()
        interpretation = self.weather_module.get_interpretation()


    pass
