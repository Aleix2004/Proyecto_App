# src/login.py
import json
import os
from hashlib import sha256

USERS_FILE = os.path.join("data", "users.json")

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def login_user(data):
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    if not email or not password:
        return False, "Email y contraseña son obligatorios."

    users = load_users()
    if email not in users:
        return False, "Email o contraseña incorrectos."

    stored_hash = users[email]["contrasena"]
    if sha256(password.encode()).hexdigest() != stored_hash:
        return False, "Email o contraseña incorrectos."

    return True, f"Bienvenido, {users[email]['nombre_completo']}!"
