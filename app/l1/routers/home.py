# routers/home.py

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

@router.get("/")
async def get_html_root(req:Request):
    resp = templates.TemplateResponse(
        request=req,
        name="home/home.html",
        context={}
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