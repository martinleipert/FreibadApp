import requests
import json
import datetime

"""
Martin Leipert
for Foerderverein Freibad Graefenberg

martin.leipert@t-online.de

Get data from open weather and use them for the prediction of closing and opening
"""


class WeatherModule:

    def __init__(self, config):

        weather_config = config["open_weather"]
        location_config = config["location"]

        self.__lat = location_config["lat"]
        self.__lon = location_config["lon"]
        self.__url = weather_config["url"]
        self.__api_key = weather_config["api_key"]

        self.__data = None
        self.get_update()

    def get_update(self):

        url = self.__url
        lon = self.__lon
        lat = self.__lat
        api_key = self.__api_key

        call_url = f"{url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"

        response = requests.get(call_url)
        self.__data = json.loads(response.text)
        self.__timestamp = datetime.datetime.now()

    def get_interpretation(self):
        today = self.__data["daily"][0]

        daily_max = today["temp"]["max"]
        daily_min = today["temp"]["min"]
        daily_main = today['weather'][0]["main"]

        # UV Index to get an UV radiation warning
        daily_uvi = today["uvi"]
        daily_rain = today["rain"]

        daily_wind = today["wind_speed"]

        return daily_max, daily_min, daily_rain, daily_thunderstorm, daily_category

    def is_fine(self):
        current = self.__data["current"]

    pass


if __name__ == "__main__":

    this_config = {
        "open_weather": {
            "api_key": "cb1d12b9203c27dc4e29250f755ba4d4",
            "url": "https://api.openweathermap.org/data/2.5/onecall"

        },
        "location": {
            "lat": 49.65,
            "lon": 11.25
        },
    }

    module = WeatherModule(this_config)
    module.get_update()
    daily_max, daily_min, daily_rain, daily_thunderstorm, daily_category = module.get_interpretation()
    # weather_today

    pass
