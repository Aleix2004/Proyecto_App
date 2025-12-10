from .registro import load_users, save_users 

def set_user_active(email, is_active):
    users = load_users()
    if email in users:
        users[email]['interno']['activo'] = is_active
        save_users(users)
        return True
    return False

def login_flow():
    users = load_users()
    
    for email, user_data in users.items():
        if user_data.get('interno', {}).get('activo') is True:
            print(f"\n✨ ¡Bienvenido de vuelta, {user_data['nombre_completo']}! Sesión activa encontrada.")
            return email 

    email = input("➡️ Correo Electrónico: ").strip()
    password = input("➡️ Contraseña: ").strip()

    if email not in users:
        print("Error: Correo no registrado.")
        return None
    
    user_data = users[email]
    
    if user_data['contrasena'] == password:
        set_user_active(email, True)
        print(f"\n¡Bienvenido, {user_data['nombre_completo']}! Sesión iniciada.")
        return email 
    else:
        print("Error: Contraseña incorrecta.")
        return None