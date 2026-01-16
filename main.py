# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
import uuid
from datetime import datetime

# Importamos funciones
from src.api_jikan import obtener_personajes, obtener_animes_populares
from src.scraping_anime import obtener_animes_generales  # scraping síncrono

USERS_FILE = os.path.join("data", "users.json")

app = FastAPI(title="AnimeApp Backend")

# CORS: permitir que React haga peticiones
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Schemas
# -------------------------------
class LoginSchema(BaseModel):
    email: str
    password: str

class RegisterSchema(BaseModel):
    nombre: str
    email: str
    password: str
    fecha_nacimiento: str

# -------------------------------
# Funciones auxiliares
# -------------------------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

# -------------------------------
# Endpoints
# -------------------------------

## Registro
@app.post("/register")
def api_register(data: RegisterSchema):
    users = load_users()
    email = data.email.lower()
    
    if email in users:
        return {"ok": False, "msg": "Usuario ya existe"}

    users[email] = {
        "nombre_completo": data.nombre,
        "correo": email,
        "contrasena": data.password,
        "fecha_nacimiento": data.fecha_nacimiento,
        "interno": {
            "id_individual": str(uuid.uuid4()),
            "date_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "activo": True
        }
    }

    save_users(users)
    return {"ok": True, "msg": "Usuario registrado correctamente", "email": email}

## Login
@app.post("/login")
def api_login(data: LoginSchema):
    users = load_users()
    email = data.email.lower()

    user = users.get(email)
    if not user or user["contrasena"] != data.password:
        return {"ok": False, "msg": "Usuario o contraseña incorrecta"}

    return {"ok": True, "msg": f"Bienvenido, {user['nombre_completo']}", "email": email}

## Animes populares (API)
@app.get("/animes-populares")
def api_animes_populares():
    return obtener_animes_populares()  # síncrono, devuelve lista de títulos

## Personajes de un anime (API)
@app.get("/personajes")
async def api_personajes(nombre_anime: str):
    """
    Este endpoint llama a la API de Jikan de forma asíncrona.
    """
    resultado = await obtener_personajes(nombre_anime)
    return resultado

## Animes generales (scraping)
@app.get("/animes-generales")
def api_animes_generales(limit: int = 15):
    """
    Este endpoint usa scraping de Wikipedia para devolver animes generales.
    Síncrono, no afecta la API de Jikan.
    """
    animes = obtener_animes_generales(limit)
    return {"ok": True, "animes": animes}
