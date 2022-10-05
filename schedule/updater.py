from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .job import schedule_job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_job, 'interval', minutes=1)
    scheduler.start()