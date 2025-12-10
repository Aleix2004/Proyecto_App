# src/menu.py
from .login import set_user_active

def main_menu(email):
    
    print(f"Usuario actual: {email}")
    
    while True:
        print("\nElige una opción:")
        print("1. [Acción del Sistema]")
        print("2. Cerrar Sesión")
        print("3. Salir (Deja la Sesión Activa)")
        
        choice = input("Opción: ").strip()
        
        if choice == '1':
            print("Ejecutando la Acción del Sistema...")
        elif choice == '2':
            set_user_active(email, False)
            print("Sesión cerrada correctamente.")
            return 'logout' 
        elif choice == '3':
            print("Saliendo de la terminal. Tu sesión se mantendrá ACTIVA.")
            return 'exit' 
        else:
            print("Opción no válida. Intenta de nuevo.")