import datetime
import pytz


def validate_time_difference(time) -> bool:
    """
    Function to validate that time falls within the
    +or- 2 minutes time window
    """
    curr_utc_time =  time

    ref_time = curr_utc_time - datetime.timedelta(minutes=2)

    time_diff = curr_utc_time - ref_time

    if abs(time_diff.total_seconds()) <= 120:
        # then the curr_utc_time is outside window
        return True

    return False

def get_current_utc_time() -> str:
    """
    function to go get the current time with a validation
    of + or - 2 minutes
    :return: string
    """
    utc_timezone = pytz.UTC
    curr_utc_time =  datetime.datetime.now(utc_timezone)

    if validate_time_difference(curr_utc_time):
        time_string = curr_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        return time_string

    return "Time outside 2 minutes window you might want to reset your time"

def get_current_day() -> str:
    """
    Function to get the current day of the week
    """
    current_date = datetime.datetime.now()

    day_string = current_date.strftime("%A")

    return day_string