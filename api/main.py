import os
import sys 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from router.routes import auth2
from router.routes import users
app = FastAPI()
app.include_router(auth2.root_login)
app.include_router(users.rooter)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

static_path = os.path.join(os.path.dirname(__file__),'./router/static')
templates_path = os.path.join(os.path.dirname(__file__),'./router/templates/')

app.mount("/static",StaticFiles(directory=static_path),name='static')
jina2 = Jinja2Templates(directory=templates_path)
@app.get("/signup",response_class=HTMLResponse)
async def root(request:Request):
    return jina2.TemplateResponse('registro.html',{'request':request})

@app.get("/login",response_class=HTMLResponse)
async def root(request:Request):
    return jina2.TemplateResponse('login.html',{'request':request})
