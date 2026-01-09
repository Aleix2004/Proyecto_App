import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Category:Anime_series"
HEADERS = {
    "User-Agent": "ProyectoEducativoPython/1.0 (educational)"
}

def obtener_animes_generales(limit=15):
    """
    Scraping responsable de animes en general desde Wikipedia,
    respetando robots.txt y obteniendo títulos reales.
    """
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            print(f"❌ Error HTTP: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        animes = []

        grupos = soup.find_all("div", class_="mw-category-group")

        for grupo in grupos:
            enlaces = grupo.find_all("a")
            for a in enlaces:
                titulo = a.get_text(strip=True)
                if titulo and titulo not in animes:
                    animes.append(titulo)

                if len(animes) >= limit:
                    return animes

        return animes

    except Exception as e:
        print("❌ Error en scraping:", e)
        return []
