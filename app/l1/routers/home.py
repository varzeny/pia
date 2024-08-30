# routers/home.py

# lib
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import Response

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


