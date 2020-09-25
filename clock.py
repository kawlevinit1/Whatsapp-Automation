from apscheduler.schedulers.blocking import BlockingScheduler
from hello import hello

sched = BlockingScheduler()

#scedule hello function to be called every second
sched.add_job(hello,'interval',seconds=10)
sched.start()