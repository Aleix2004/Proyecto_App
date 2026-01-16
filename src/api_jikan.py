# src/api_jikan.py
import asyncio
from aiohttp import ClientSession, ClientTimeout
from functools import lru_cache

# Cache de resultados para no sobrecargar la API
personajes_cache = {}

# Fallback manual si Jikan falla o tarda demasiado
FALLBACK_PERSONAJES = {
    "Chainsaw Man": ["Denji", "Power", "Makima", "Aki Hayakawa"],
    "Sousou no Frieren": ["Frieren", "Fern", "Eisen", "Hauptmann"],
    "Steins;Gate": ["Okabe Rintarou", "Makise Kurisu", "Mayuri Shiina", "Daru"],
    "Fullmetal Alchemist: Brotherhood": ["Edward Elric", "Alphonse Elric", "Roy Mustang", "Winry Rockbell"],
    "Hunter x Hunter (2011)": ["Gon Freecss", "Killua Zoldyck", "Kurapika", "Leorio Paradinight"],
    "Shingeki no Kyojin Season 3 Part 2": ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi"],
    "Gintama°": ["Gintoki Sakata", "Shinpachi Shimura", "Kagura", "Tae Shimura"],
    "One Piece": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Sanji"],
}

@lru_cache(maxsize=32)
def obtener_animes_populares():
    """Retorna lista de animes populares"""
    animes = [
        "Chainsaw Man",
        "Sousou no Frieren",
        "Fullmetal Alchemist: Brotherhood",
        "Steins;Gate",
        "Shingeki no Kyojin Season 3 Part 2",
        "Gintama°",
        "Hunter x Hunter (2011)",
        "One Piece"
    ]
    return {"ok": True, "animes": animes}


async def fetch_json(url, params=None):
    """Hace request GET a Jikan con timeout"""
    timeout = ClientTimeout(total=30)  # hasta 30s de espera
    async with ClientSession(timeout=timeout) as session:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                raise Exception(f"Error {resp.status} en {url}")
            return await resp.json()


async def obtener_personajes(nombre_anime: str):
    """Obtiene personajes de un anime, con fallback y cache"""
    if nombre_anime in personajes_cache:
        return {"ok": True, "personajes": personajes_cache[nombre_anime]}

    try:
        url_search = "https://api.jikan.moe/v4/anime"
        params = {"q": nombre_anime, "limit": 1}
        data = await fetch_json(url_search, params)

        if not data.get("data"):
            personajes = FALLBACK_PERSONAJES.get(nombre_anime, [])
        else:
            anime_id = data["data"][0]["mal_id"]
            url_chars = f"https://api.jikan.moe/v4/anime/{anime_id}/characters"
            char_data = await fetch_json(url_chars)
            personajes = [c["character"]["name"] for c in char_data.get("data", []) if "character" in c]

            if not personajes:  # fallback si API no devuelve nada
                personajes = FALLBACK_PERSONAJES.get(nombre_anime, [])

    except Exception as e:
        print(f"Error al obtener personajes de '{nombre_anime}': {e}")
        personajes = FALLBACK_PERSONAJES.get(nombre_anime, [])

    personajes_cache[nombre_anime] = personajes
    return {"ok": True, "personajes": personajes}
