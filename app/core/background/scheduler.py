# scheduler.py

# lib
from typing import Callable, Any
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# module
import app.core.database as DB
import app.l2.trend as TREND

# attribute

SCHEDULER = AsyncIOScheduler()

# method
def activate():
    SCHEDULER.start()

def deactivate():
    SCHEDULER.shutdown()


def set_func_to_timer(func:Callable[..., Any], name:str, hour:int, min:int):
    
    SCHEDULER.add_job(
        func=func,
        trigger=CronTrigger(hour=hour, minute=min),
        id=name,
        replace_existing=True # 같은 이름의 작업 덮어쓰기
    )



async def get_trends_by_country_all():
    print("스케쥴러에 의해 호출됨")
    try:
        trends = []
        for country in TREND.COUNTRIES:
            trend_data = await TREND.get_trends_by_country(country)
       
            # db 저장
            trends.append(
                DB.Trend(
                    country=country,
                    rank_1=trend_data[0],
                    rank_2=trend_data[1],
                    rank_3=trend_data[2],
                    rank_4=trend_data[3],
                    rank_5=trend_data[4],
                    rank_6=trend_data[5],
                    rank_7=trend_data[6],
                    rank_8=trend_data[7],
                    rank_9=trend_data[8],
                    rank_10=trend_data[9],
                    rank_11=trend_data[10],
                    rank_12=trend_data[11],
                    rank_13=trend_data[12],
                    rank_14=trend_data[13],
                    rank_15=trend_data[14],
                    rank_16=trend_data[15],
                    rank_17=trend_data[16],
                    rank_18=trend_data[17],
                    rank_19=trend_data[18],
                    rank_20=trend_data[19]
                )
            )

        async for ss in DB.get_ss():
            ss.add_all(trends)
            await ss.commit()

    except Exception as e:
        print("ERROR form get_trends_by_country_all : ", e)
        return None

