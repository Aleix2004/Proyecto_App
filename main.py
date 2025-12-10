# main.py

import sys
import os

# -------------------------------------------------------------------
# --- CORRECCIÓN CRUCIAL DE RUTA PARA IMPORTACIÓN DE PAQUETES ---
# Se debe hacer ANTES de cualquier importación de módulo local
# -------------------------------------------------------------------
sys.path.append(os.path.dirname(__file__)) 

# --- IMPORTACIONES ADAPTADAS AL NUEVO NOMBRE DE ARCHIVO ---
from src.registro import register_flow  # Importa registro.py
from src.login import login_flow        # Importa login.py
from src.menu import main_menu          # Importa menu.py


def run_project():
    """Bucle principal del sistema de autenticación."""
    current_user_email = None

    while True:
        # 1. Intenta iniciar sesión (o recupera sesión activa)
        if current_user_email is None:
            current_user_email = login_flow()

        if current_user_email:
            # 2. Si hay un usuario, ir al menú de la aplicación
            action = main_menu(current_user_email)
            
            if action == 'logout':
                current_user_email = None 
            elif action == 'exit':
                break 

        else:
            # 3. Menú de Login/Registro si no hay sesión activa
            print("\n==================================")
            print("  SISTEMA DE AUTENTICACIÓN PYTHON ")
            print("==================================")
            print("Elige una opción:")
            print("1. Iniciar Sesión")
            print("2. Registrar Nuevo Usuario")
            print("3. Salir del programa")
            
            choice = input("Opción: ").strip()

            if choice == '1':
                continue 
            elif choice == '2':
                register_flow()
            elif choice == '3':
                print("👋 Saliendo del sistema. ¡Adiós!")
                break
            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    run_project()