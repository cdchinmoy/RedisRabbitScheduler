import os
import time
from job import first_job, second_job
from datetime import datetime
import schedule
from time_format import get_utc_time, get_24hr_format, get_scheduler_time_format

timezone = os.environ['TIMEZONE']

time1 = get_24hr_format('06:00 PM')
time2 = get_24hr_format('09:00 PM')
today = datetime.today().strftime('%Y-%m-%d')
first_schedule_time = today + " " + time1
second_schedule_time = today + " " + time2

utc_first_schedule_datetime_obj = get_utc_time(timezone, first_schedule_time)
utc_second_schedule_datetime_obj = get_utc_time(timezone, second_schedule_time)

utc_first_schedule_time = get_scheduler_time_format(utc_first_schedule_datetime_obj)
utc_second_schedule_time = get_scheduler_time_format(utc_second_schedule_datetime_obj)

# schedule.every(1).minutes.do(first_job)
schedule.every().day.at(utc_first_schedule_time).do(first_job)
schedule.every().day.at(utc_second_schedule_time).do(second_job)


while True:
    schedule.run_pending()
    time.sleep(1)