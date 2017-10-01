from apscheduler.schedulers.blocking import BlockingScheduler
import requests


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    requests.get("https://aps8train.herokuapp.com/api/update-lines")
    print('CRON - Updated LOG')


sched.start()
