import datetime


class ScheduleModule:

    # Initialize with the schedule from configuration
    def __init__(self, config):

        current_year = datetime.date.today().year

        season = config["season"]
        season_start = season["start"]
        season_end = season["end"]

        self.season_start = datetime.date(current_year, season_start["month"], season_start["day"])
        self.season_end = datetime.date(current_year, season_end["month"], season_end["day"])

        hours = config["hours"]
        opening = hours["opening_hour"]
        closing = hours["closing_hour"]

        self.opening_hour = datetime.time.fromisoformat(opening)
        self.closing_hour = datetime.time.fromisoformat(closing)

    def is_season(self):

        # Get today's day of year
        today = datetime.date.today()
        today = today.timetuple().tm_yday

        # Convert to day of year
        start_date = self.season_start.timetuple().tm_yday
        end_date = self.season_end.timetuple().tm_yday

        # Out of season
        if (today < start_date) and (end_date < today):
            return False

        # Inside season
        return True

    def is_shedule(self):

        now = datetime.datetime.now()
        now = now.time()

        opening = self.opening_hour
        closing = self.closing_hour

        # Check if we are outside the shedule
        if (now < opening) and (closing < now):
            return False

        return True

    def is_open(self):
        """
        Checks if Freibad is open according to shedule
        :return: Boolean value indicating if it is open (True) oder closed (False)
        """

        # First exclusion criteria: Season
        if not self.is_season():
            return False

        # Second exclusion criteria: Shedule
        if not self.is_shedule():
            return False

        return True

