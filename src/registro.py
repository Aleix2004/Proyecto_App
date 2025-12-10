# src/registro.py
import re
import json
import os
from datetime import datetime
import uuid

# --- CONFIGURACIÓN Y CONSTANTES (Igual que antes) ---
DB_FILE_PATH = os.path.join('data', 'users.json')

MIN_NUMEROS = 3
MIN_ESPECIALES = 2
CARACTERES_ESPECIALES = r'@$!%*?&#' 

PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d){%s}(?=(?:.*[%s]){%s})[A-Za-z\d%s]{8,}$"
    % (MIN_NUMEROS, re.escape(CARACTERES_ESPECIALES), MIN_ESPECIALES, re.escape(CARACTERES_ESPECIALES))
)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# --- FUNCIONES DE I/O Y UTILIDAD (Exportadas) ---

def load_users():
    """Carga los datos de usuarios desde el archivo JSON."""
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(DB_FILE_PATH) or os.path.getsize(DB_FILE_PATH) == 0:
        return {}
    try:
        with open(DB_FILE_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_users(users):
    """Guarda los datos de usuarios en el archivo JSON."""
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(DB_FILE_PATH, 'w') as f:
        json.dump(users, f, indent=4)

def display_password_rules():
    """Muestra las reglas de la contraseña."""
    print("\n--- REQUISITOS DE CONTRASEÑA ---")
    print("* Longitud mínima: **8 caracteres**")
    print("* Debe contener: **Mayúsculas** y **Minúsculas**")
    print(f"* Mínimo **{MIN_NUMEROS} números**.")
    print(f"* Mínimo **{MIN_ESPECIALES} caracteres especiales** (permitidos: {CARACTERES_ESPECIALES}).")
    print("---------------------------------")

# --- FUNCIONES DE VALIDACIÓN ---

def validate_password(password):
    if not PASSWORD_REGEX.fullmatch(password):
        print("❌ Error: La contraseña no cumple con todos los requisitos de seguridad.")
        display_password_rules()
        return False
    return True

def validate_email(email, users):
    if not EMAIL_REGEX.fullmatch(email):
        print("❌ Error: Formato de correo electrónico inválido.")
        return False
    if email in users:
        print("❌ Error: Este correo electrónico ya está registrado.")
        return False
    return True

# --- FUNCIÓN PRINCIPAL DE REGISTRO ---

def register_flow():
    """Flujo interactivo para el registro de usuario."""
    users = load_users()
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    
    nombre_completo = input("➡️ Nombre Completo: ").strip()

    while True:
        email = input("➡️ Correo Electrónico: ").strip()
        if validate_email(email, users):
            break

    while True:
        password = input("➡️ Contraseña: ").strip()
        if validate_password(password):
            password_x2 = input("➡️ Repite la Contraseña: ").strip()
            if password == password_x2:
                break
            else:
                print("❌ Error: Las contraseñas no coinciden. Intenta de nuevo.")

    fecha_nacimiento = input("➡️ Fecha de Nacimiento (ej: 01/01/2000): ").strip()
    
    # --- CREACIÓN DE DATA INTERNA ---
    user_id = str(uuid.uuid4())
    date_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_user_data = {
        'nombre_completo': nombre_completo,
        'correo': email,
        'contrasena': password,
        'fecha_nacimiento': fecha_nacimiento,
        'interno': {
            'id_individual': user_id,
            'date_registro': date_registro,
            'activo': False
        }
    }
    
    users[email] = new_user_data
    save_users(users)
    print("\n✅ ¡Registro exitoso! Ahora puedes iniciar sesión.")
    return True