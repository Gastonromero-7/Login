from fastapi import APIRouter,Form,Request,Cookie
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from client.client import db_client
from routes.schemes.user import user_schemes_db,user_schemes
from routes.models.users import User_db,User
from datetime import datetime,timezone,timedelta
import jwt

root_login = APIRouter()
jina2 = Jinja2Templates(directory="templates")
ouath2 = OAuth2PasswordBearer(tokenUrl="login")

SECRET = "9b9d06e6dffd63f2fa6eee2e04b07dc6732f0381c4cdeb3f85ee79b76850c7f1"

ALGORITHM = "HS256"

TOKEN_SCONDS_EXP = 30

crypt = CryptContext(schemes=["bcrypt"])

def search_user(username):
    try:
        user = user_schemes(db_client.users.find_one({"username":username}))
        return User(**user)
    except:
        return "Error"
def search_user_db(username):
    try:
        user = user_schemes_db(db_client.users.find_one({"username":username}))
        return User_db(**user)
    except:
        return "Error"
    
@root_login.post("/login")
async def login (username : Annotated[str,Form()],password:Annotated[str,Form()],request:Request):
    users = db_client.users.find_one({"username":username})
    if not users:
        return jina2.TemplateResponse("login.html",
                                            {"request":request,
                                            "insuccess":True}   )
    user_db = search_user_db(username)
    if not crypt.verify(password,user_db.password):
        return jina2.TemplateResponse("login.html",
                                            {"request":request,
                                            "insuccess":True
                                            }   )
    expire = datetime.now(timezone.utc) + timedelta(seconds=TOKEN_SCONDS_EXP)

    access_token = {"sub":user_db.username,
                    "exp":expire
                }
    token =  jwt.encode(access_token,SECRET,algorithm=ALGORITHM) 
    return RedirectResponse("/auth/dashboard",
                            status_code=302,
                            headers={"set-cookie":f"access_token={token}; Max-Age = {TOKEN_SCONDS_EXP}"})

@root_login.post("/logout")
async def logout(token:Annotated[str | None, Cookie()]=None):
    return RedirectResponse("/auth",
                            status_code=302,
                            headers={"set-cookie":f"access_token={token}; Max-Age =0"})
    
@root_login.get("/auth")
async def login_great(request:Request):
    return jina2.TemplateResponse("login.html",{"request":request})

@root_login.get("/auth/dashboard")
async def auth_login(request:Request,access_token:Annotated[str | None, Cookie()]=None):
    if not access_token:
        return RedirectResponse("/auth",
                                status_code=302)
    return jina2.TemplateResponse("index.html",{"request":request})