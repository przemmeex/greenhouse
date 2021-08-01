import json
import os
from datetime import datetime


def read_config():
    """Load configuration from file

    :return: Configuration
    :rtype: dictionary
    """
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "app_config.json"), "r") as read_file:
        config = json.load(read_file)
    return config


def time_to_day_seconds(time):
    """Convert time in format "%H:%M:%S" to seconds form midnight

    :param time: time in format "%H:%M:%S"
    :type time: string
    :return: Seconds from last midnight
    :rtype: int
    """
    seconds_past = (int(time.split(":")[0])*3600
                    + int(time.split(":")[1])*60
                    + int(time.split(":")[2]))
    return seconds_past


def is_day():
    """Check if currently is day

    :return: true if now is day
    :rtype: bool
    """
    config = read_config()
    current_time = time_to_day_seconds(datetime.now().strftime("%H:%M:%S"))
    day_start = time_to_day_seconds(config["dayStart"])
    day_duration = time_to_day_seconds(config["dayDuration"])
    whole_day = 24 * 3600

    if(day_start + day_duration > whole_day):
        light_periods = [(0, day_duration + day_start -
                          whole_day), (day_start, whole_day)]
    else:
        light_periods = [(day_start, day_start + day_duration)]

    for period in light_periods:
        if current_time in range(period[0], period[1]):
            return True
    return False
