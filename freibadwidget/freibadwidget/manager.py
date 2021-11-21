from ..modules.config import config
from ..modules.weather import WeatherModule


class StatusManager:

    def __init__(self):

        self.__weather = WeatherModule(config)
        pass

    def update_status(self):

        pass

