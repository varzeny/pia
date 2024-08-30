# main.py

# lib
from fastapi import FastAPI, staticfiles

from dotenv import load_dotenv

# module
from app.l1.routers.home import router as router_home


# method
async def startup():
    # database

    # authorization

    print()


async def shutdown():
    print()


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

# env
application.state.env = load_dotenv()



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:application",
        host="0.0.0.0",
        port=9000,
        reload=True
    )
    
    print()