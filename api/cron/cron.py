import logging

from apscheduler.schedulers.blocking import BlockingScheduler
import requests

logger = logging.getLogger(__name__)

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=15)
def timed_job():
    requests.get("https://aps8train.herokuapp.com")
    print('CRON - Updated LOG')
    logger.error("Running CRON")


sched.start()
