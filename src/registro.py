# src/registro.py
import json
import os
import re
from hashlib import sha256
from datetime import datetime
import uuid

USERS_FILE = os.path.join("data", "users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def register_user(data):
    nombre = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    if not nombre or not email or not password:
        return False, "Todos los campos son obligatorios."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Email inválido."
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."

    users = load_users()
    if email in users:
        return False, "El email ya está registrado."

    users[email] = {
        "nombre_completo": nombre,
        "correo": email,
        "contrasena": sha256(password.encode()).hexdigest(),
        "fecha_nacimiento": data.get("fecha_nacimiento", ""),
        "interno": {
            "id_individual": str(uuid.uuid4()),
            "date_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "activo": True
        }
    }

    save_users(users)
    return True, "Usuario registrado correctamente."
