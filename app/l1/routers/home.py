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

# attribute
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# method

@router.get("/")
async def get_html_root(req:Request, ss:AsyncSession=Depends(DB.get_ss)):
    # 먼저 가장 최근의 created_at 값을 가져옴
    subquery = select(DB.Trend.created_at).order_by(desc(DB.Trend.created_at)).limit(1).subquery()
    
    # 그 created_at 값과 일치하는 모든 행을 가져옴
    result = await ss.execute(
        select(DB.Trend).where(DB.Trend.created_at == subquery.c.created_at)
    )
    
    recent_trends = result.scalars().all()  # 모든 해당 행을 리스트로 가져옴
    print(recent_trends)


    resp = templates.TemplateResponse(
        request=req,
        name="home/home.html",
        context={
            "trends":recent_trends
        }
    )
    return resp


@router.get("/about")
async def get_html_about(req:Request):
    p = os.path.join(os.path.dirname(__file__), "../../../", "README.md")
    readme = UTIL.read_markdown_from_file(p)

    resp = templates.TemplateResponse(
        request=req,
        name="home/about.html",
        context={
            "readme":readme
        }
    )
    return resp