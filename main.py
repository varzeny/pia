# main.py


# lib
from fastapi import FastAPI, staticfiles

from dotenv import load_dotenv

# module
import app.core.background.scheduler as SCHE
import app.core.database as DB
from app.l1.routers.home import router as router_home
from app.l1.routers.trend import router as router_trend

import app.l2.trend as TREND

# method
async def startup():
    # script
    # alembic revision --autogenerate -m "update" 
    # alembic upgrade head 

    # env
    load_dotenv()

    # scheduler
    SCHE.activate()
    SCHE.set_func_to_timer(
        func=SCHE.get_trends_by_country_all,
        name="get_trends_by_country_all",
        hour=0,
        min=0
    )
    
    # l2 trend의 함수 추가
    # SCHE.set_func_to_timer(
    #     TREND.get_trends_by_country_all, "get_trend_all", 0, 0
    # )


    # database
    async with DB.ENGINE.begin() as conn:
        await conn.run_sync( DB.BASE.metadata.create_all )

    # authorization


async def shutdown():
    # scheduler
    SCHE.deactivate()



# attribute
application = FastAPI(
    on_startup=[ startup ],
    on_shutdown=[ shutdown ]
)

# 정적파일
application.mount(
    path="/static",
    app=staticfiles.StaticFiles(directory="app/staticfiles"),
    name="static_files"
)

# 미들웨어
# application.add_middleware()

# 라우터
application.include_router( router_home )
application.include_router( router_trend )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:application",
        host="0.0.0.0",
        port=9000,
        reload=True
    )
    
    print()