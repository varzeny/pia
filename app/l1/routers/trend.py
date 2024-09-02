# routers/trend.py

# lib
import os, asyncio
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

# module
import app.core.database as DB
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


@router.get("/test")
async def test(req:Request, ss:AsyncSession=Depends(DB.get_ss)):
    print("tttttttttttttttttttttttttttttt")
    ss.add( DB.Test(name="lee") )
    await ss.commit()

