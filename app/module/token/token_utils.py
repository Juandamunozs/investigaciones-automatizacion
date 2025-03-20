import json
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from env.env import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, dir_db_json
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose.exceptions import ExpiredSignatureError, JWTError
import bcrypt
import os

# Configurar el esquema OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Cifrado de contraseñas con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para cargar usuarios desde el archivo JSON
def cargar_usuarios():
    if not os.path.exists(dir_db_json):
        return {}  # Si el archivo no existe, retorna un diccionario vacío
    with open(dir_db_json, "r", encoding="utf-8") as file:
        return json.load(file)

# Función para guardar usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open(dir_db_json, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4)

# Función para autenticar usuarios
def authenticate_user(username: str, password: str):
    usuarios = cargar_usuarios()
    usuario = usuarios.get(username)

    if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario["password"].encode('utf-8')):
        return usuario

    return None  

# Función para obtener el rol del usuario
def obtener_rol(username: str):
    usuarios = cargar_usuarios()
    usuario = usuarios.get(username)
    return usuario["rol"] if usuario else None

# Función para crear el token de acceso
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Función para verificar el token
def verificar_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token sin usuario")
        return username
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado.")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido.")

# Función para hashear contraseñas
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Función para registrar un usuario en el JSON
def registrar_usuario(username: str, password: str, rol: str):
    usuarios = cargar_usuarios()
    if username in usuarios:
        return "Usuario ya existe."

    hashed_password = hash_password(password)
    usuarios[username] = {"password": hashed_password, "rol": rol}
    guardar_usuarios(usuarios)
    return "Usuario registrado exitosamente."
