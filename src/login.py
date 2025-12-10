# src/login.py
# Importación relativa: desde el mismo paquete (src), importa registro.py
from .registro import load_users, save_users 

def set_user_active(email, is_active):
    """Actualiza el booleano 'activo' del usuario en la base de datos."""
    users = load_users()
    if email in users:
        users[email]['interno']['activo'] = is_active
        save_users(users)
        return True
    return False

def login_flow():
    """Flujo interactivo para el inicio de sesión."""
    users = load_users()
    
    # Comprobar si hay un usuario activo (Sesión persistente)
    for email, user_data in users.items():
        if user_data.get('interno', {}).get('activo') is True:
            print(f"\n✨ ¡Bienvenido de vuelta, {user_data['nombre_completo']}! Sesión activa encontrada.")
            return email 

    print("\n--- INICIO DE SESIÓN ---")
    email = input("➡️ Correo Electrónico: ").strip()
    password = input("➡️ Contraseña: ").strip()

    if email not in users:
        print("❌ Error: Correo no registrado.")
        return None
    
    user_data = users[email]
    
    if user_data['contrasena'] == password:
        set_user_active(email, True)
        print(f"\n🎉 ¡Bienvenido, {user_data['nombre_completo']}! Sesión iniciada.")
        return email 
    else:
        print("❌ Error: Contraseña incorrecta.")
        return None