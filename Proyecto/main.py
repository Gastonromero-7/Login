from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from routers import users,auth2


app = FastAPI()
app.include_router(users.rooter)
app.include_router(auth2.root_login)

static_path = os.path.join(os.path.dirname(__file__),'./static')
templates_path = os.path.join(os.path.dirname(__file__),'./templates/')

app.mount("/static",StaticFiles(directory=static_path),name='static')
jina2 = Jinja2Templates(directory=templates_path)
@app.get("/signup",response_class=HTMLResponse)
async def root(request:Request):
    return jina2.TemplateResponse('registro.html',{'request':request})

@app.get("/login",response_class=HTMLResponse)
async def root(request:Request):
    return jina2.TemplateResponse('login.html',{'request':request})
