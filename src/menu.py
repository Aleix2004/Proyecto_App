from .login import set_user_active
from .api_jikan import obtener_personajes, obtener_animes_populares
from .scraping_anime import obtener_animes_generales

ANIMES_EJEMPLO = {
    "Naruto": 20,
    "Naruto Shippuden": 1735,
    "One Piece": 21,
    "Bleach": 269,
    "Dragon Ball": 813,
    "Attack on Titan": 16498,
    "Fullmetal Alchemist: Brotherhood": 5114
}

def mostrar_personajes():
    print("\nAnimes disponibles para elegir:")
    for nombre, anime_id in ANIMES_EJEMPLO.items():
        print(f"{nombre} (ID: {anime_id})")

    try:
        anime_id = int(input("\nIngresa el ID del anime que quieres ver: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    print("\nObteniendo personajes desde la API Jikan...\n")
    personajes = obtener_personajes(anime_id=anime_id, limit=10)

    if not personajes:
        print("❌ No se pudieron obtener personajes.")
        return

    print("=== PERSONAJES DEL ANIME ===")
    for p in personajes:
        nombre = p.get("character", {}).get("name", "Desconocido")
        rol = p.get("role", "Desconocido")
        print(f"\nNombre: {nombre}")
        print(f"Rol: {rol}")
        print("-" * 40)

def mostrar_animes_populares():
    print("\nObteniendo animes más populares...\n")
    animes = obtener_animes_populares(limit=10)

    if not animes:
        print("❌ No se pudieron obtener los animes.")
        return

    print("=== ANIMES POPULARES (API) ===")
    for a in animes:
        nombre = a.get("title", "Desconocido")
        score = a.get("score", "N/A")
        print(f"\nNombre: {nombre}")
        print(f"Puntaje: {score}")
        print("-" * 40)

def mostrar_animes_scraping():
    print("\nObteniendo animes mediante scraping desde Wikipedia...\n")
    animes = obtener_animes_generales(limit=15)

    if not animes:
        print("❌ No se pudieron obtener datos.")
        return

    print("=== ANIMES (SCRAPING) ===")
    for i, anime in enumerate(animes, 1):
        print(f"{i}. {anime}")

def main_menu(email):
    print(f"Usuario actual: {email}")
    
    while True:
        print("\nElige una opción:")
        print("1. Ver personajes de un anime (API)")
        print("2. Ver animes más populares (API)")
        print("3. Ver animes (Scraping)")
        print("4. Cerrar Sesión")
        print("5. Salir (Deja la Sesión Activa)")
        
        choice = input("Opción: ").strip()
        
        if choice == '1':
            mostrar_personajes()
        elif choice == '2':
            mostrar_animes_populares()
        elif choice == '3':
            mostrar_animes_scraping()
        elif choice == '4':
            set_user_active(email, False)
            print("Sesión cerrada correctamente.")
            return 'logout'
        elif choice == '5':
            print("Saliendo de la terminal. Tu sesión se mantendrá ACTIVA.")
            return 'exit'
        else:
            print("Opción no válida. Intenta de nuevo.")
