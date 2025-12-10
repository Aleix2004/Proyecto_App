import sys
import os

sys.path.append(os.path.dirname(__file__)) 

from src.registro import register_flow  
from src.login import login_flow        
from src.menu import main_menu          


def run_project():
    current_user_email = None

    while True:
        if current_user_email is None:
            current_user_email = login_flow()

        if current_user_email:
            action = main_menu(current_user_email)
            
            if action == 'logout':
                current_user_email = None 
            elif action == 'exit':
                break 

        else:

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
                print("Saliendo del sistema. ¡Adiós!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    run_project()