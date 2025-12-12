# src/api_jikan.py
import requests

BASE_URL = "https://api.jikan.moe/v4"

def obtener_personajes(anime_id, limit=10):
    """
    Obtiene los personajes de un anime usando Jikan API.
    :param anime_id: ID del anime en MyAnimeList
    :param limit: Número máximo de personajes a retornar
    """
    url = f"{BASE_URL}/anime/{anime_id}/characters"
    
    try:
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code != 200:
            print("❌ Error al conectar con la API:", respuesta.status_code)
            return []

        data = respuesta.json()
        personajes = data.get("data", [])
        return personajes[:limit]

    except Exception as e:
        print("❌ Error al procesar la API:", e)
        return []

def obtener_animes_populares(limit=10):
    """
    Obtiene los animes más populares usando Jikan API
    """
    url = f"{BASE_URL}/top/anime"
    try:
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code != 200:
            print("❌ Error al conectar con la API:", respuesta.status_code)
            return []

        data = respuesta.json()
        animes = data.get("data", [])
        return animes[:limit]

    except Exception as e:
        print("❌ Error al procesar la API:", e)
        return []
