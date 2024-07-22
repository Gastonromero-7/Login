from passlib.context import CryptContext
crypt = CryptContext(schemes=["bcrypt"])
def user_schemes_db(user):
    return {
            "username":user["username"],
            "email":user["email"],
            "password":user["password"]}
def user_schemes_dbb(user):
    mensaje = f"{user["password"]}"
    mensaje_encriptado = mensaje.encode()
    encriptar = crypt.hash(mensaje_encriptado)
    return {
            "username":user["username"],
            "email":user["email"],
            "password":encriptar
            }

def user_schemes(user):
    return {
            "username":user["username"],
            "email":user["email"]
            }

def user(user):
    return[user_schemes_db(users) for users in user]