# routers/home.py

# lib
import os
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,desc

# module
import app.core.util as UTIL
import app.core.database as DB

# define
router = APIRouter( prefix="/widget" )
templates = Jinja2Templates(directory="app/templates")


@router.get("/summary")
async def get_summary(req:Request, ss:AsyncSession=Depends(DB.get_ss)):

    result = await ss.execute(
        select(DB.Trend)
        .where(DB.Trend.country=="south_korea")
        .order_by( desc(DB.Trend.created_at) )
        .limit(1)
    )
    summary = result.scalars().all()
    print( summary.rank_1 )
    print( summary.rank_2 )
    print( summary.rank_3 )


    resp = templates.TemplateResponse(
        request=req,
        name="/trend/summary.html",
        context={"summary":summary}
    )
    return resp