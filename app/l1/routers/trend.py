# routers/trend.py

# lib
import os
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response

# module
import app.l2.util as UTIL

# attribute
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# method

@router.get()
async def get_():
    return