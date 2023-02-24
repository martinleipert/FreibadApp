from ..modules.config import config
from ..modules.weather import WeatherModule
from ..modules.schedule import ScheduleModule
import threading
from .models import Day

import datetime
import logging


class StatusManager:

    def __init__(self):

        # Get a module to check the opening hours
        self.__schedule = ScheduleModule(config)

        self.__weather = WeatherModule(config)

        # Update every 15 minutes
        self.__timer = threading.Timer(900, self.update_status)

        self.__today = Day()

        self.__logger = logging.Logger("Main_Logger")

    def update_status(self, request):
        current_time = datetime.datetime.now()

        self.__weather.get_update()
        daily_max, daily_min, daily_rain, daily_thunderstorm, daily_category = self.__weather.get_interpretation()

        # New day object if midnight has passed
        if self.__today.date != current_time.date():
            self.__today.save(force_update=True)

            self.__today = Day()
            self.__today.date = current_time.date()

        self.__schedule.update(current_time)

        pass

    def run_open_check(self):

        # Check if the date is valid opening hour to shedule
        if not self.__schedule.is_open():
            return False

        if not self.__weather.is_fine():
            return False

        return True

    def get_logger(self):
        return self.__logger
