import time
from job import first_job, second_job
import schedule

#Time should UTC & frormat should be HH:MM:SS
# schedule.every(1).minutes.do(first_job)
schedule.every().day.at("10:02:00").do(first_job)
schedule.every().day.at("10:03:00").do(second_job)

while True:
    schedule.run_pending()
    time.sleep(1)