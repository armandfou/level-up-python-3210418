import sched
import time
from datetime import datetime


def schedule_function(event_time, function, *args):
  scheduler = sched.scheduler(time.time, time.sleep)
  scheduler.enterabs(  event_time.timestamp(), 1, function, args)
  scheduler.run()

  
  
def hello():
  print("ggggggggggggggg")
 
schedule_function(datetime(2024, 9, 8, 0, 28), hello, None)