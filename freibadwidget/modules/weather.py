import requests
import json
import datetime


class WeatherModule:

    def __init__(self, config):

        weather_config = config["open_weather"]

        self.__lat = weather_config["lat"]
        self.__lon = weather_config["lon"]
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

        daily_rain =

        return daily_max

    pass


if __name__ == "__main__":

    this_config = {
        "open_weather": {
            "api_key": "cb1d12b9203c27dc4e29250f755ba4d4",
            "lat": 49.65,
            "lon": 11.25,
            "url": "https://api.openweathermap.org/data/2.5/onecall"
        },
    }

    module = WeatherModule(this_config)
    data = module.get_update()
    data.get_interpretation
    # weather_today

    pass
