# routers/trend.py

# lib
import os, asyncio
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

# module
import app.l2.trend as TREND


# attribute
router = APIRouter(
    prefix="/trend"
)
templates = Jinja2Templates(directory="app/templates")

# method

@router.get("/")
async def get_trend(req:Request):
    country = req.query_params.get("country")
    print("======", country)

    # respData = {}

    # if country == "all":
    #     for c in TREND.COUNTRIES:
    #         result = await asyncio.to_thread( TREND.get_trends_by_country, c )
    #         if result:
    #             respData[c] = result
    # else:
    #     result = await asyncio.to_thread( TREND.get_trends_by_country, country )
    #     if result:
    #         respData[country] = result

    # if not result:
    #     return Response(status_code=400)
    # else:
    #     return JSONResponse(content=respData)