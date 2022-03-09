import pytz
from datetime import datetime

def get_24hr_format(time):
    in_time = datetime.strptime(time, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time

def get_utc_time(timezone, time):
    local = pytz.timezone(timezone)
    naive = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt

def get_scheduler_time_format(date_time):
    data = date_time.strftime("%H:%M:%S")
    return data