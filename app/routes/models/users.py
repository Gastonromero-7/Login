from pydantic import BaseModel,Field,field_validator
class User(BaseModel):
    username : str
    email : str 

class User_db(User):
    password:str = Field(min_length=6,description="La contraseña debe tener al menos 6 caracteres")
    @field_validator("password")
    def password_length(cls, v):
        if len(v) < 6:
            raise ValueError('La contraseña debe tener al menos 6 caracteres')
        return v
