from fastapi import APIRouter,Form,HTTPException,status,Request
from router.client.client import user_collection
from fastapi.responses import RedirectResponse,HTMLResponse
from typing import Annotated
from router.routes.schemes.user import user_schemes_db,user_schemes,user_schemes_dbb
from router.routes.models.users import User,User_db
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

rooter = APIRouter()
TOKEN_SCONDS_EXP = 2

jina2 = Jinja2Templates(directory="router/templates")
@rooter.post("/signup",response_class=HTMLResponse)
async def create_user(username:Annotated[str,Form()],email:Annotated[str,Form()],password:Annotated[str,Form()],request:Request):
    if type(search_user_db("email",email)) == User_db:
        return jina2.TemplateResponse("registro.html",
                                      {"request":request,
                                       "success":False,
                                       "error":"Usuario ya creado"}   )
    
    sign_user = {"username":username,
                 "email":email,
                 "password":password}
    try:
        new_user = user_schemes_dbb(dict(sign_user))
    except ValidationError as e:
        return jina2.TemplateResponse("registro.html",{"request":request,"success": False, "error": e.errors()[0]['msg']})

    id = user_collection.insert_one(new_user).inserted_id

    user_schemes_dbb(user_collection.find_one({"_id":id}))

    return RedirectResponse("/login",
                            status_code=302)


def search_user(field:str,key:str):
    try:
        user = user_schemes(user_collection.find_one({field:key}))
        return User(**user)
    except:
        return "Error"
    
def search_user_db(field:str,key:str):
    try:
        user = user_schemes_db(user_collection.find_one({field:key}))
        return User_db(**user)
    except:
        return "Error"
    




