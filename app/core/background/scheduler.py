# scheduler.py

# lib
from typing import Callable, Any
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# module
import app.core.database as DB

# attribute

SCHEDULER = AsyncIOScheduler()

# method
def activate():
    SCHEDULER.start()

def deactivate():
    SCHEDULER.shutdown()

# 매번 호출되는거임
def set_func_to_timer(func:Callable[..., Any], name:str, hour:int, min:int):
    SCHEDULER.add_job(
        func=func,
        args=(DB.get_ss()), # 위치인자
        trigger=CronTrigger(hour=hour, min=min),
        id=name,
        replace_existing=True # 같은 이름의 작업 덮어쓰기
    )





