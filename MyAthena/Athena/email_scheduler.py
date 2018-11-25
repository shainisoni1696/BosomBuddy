from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
sched= BlockingScheduler()

def my_interval_job():
        subprocess.call(["bash","email.sh"])
sched.add_job(my_interval_job,'interval',seconds=30)
sched.start()
