🎌 AnimeApp

AnimeApp es una aplicación web full-stack que permite explorar animes populares y consultar los personajes de cada anime utilizando una API externa y web scraping, manteniendo ambas fuentes totalmente separadas.

Descripción del Proyecto

La aplicación muestra una lista de animes y permite al usuario ver los personajes asociados a cada uno.
    Los personajes se obtienen mediante la API de Jikan (MyAnimeList)
    El web scraping se usa únicamente para obtener información general de animes
    No se mezclan datos entre scraping y API, respetando buenas prácticas

Tecnologías Utilizadas:
    Frontend
    React
    Vite
    JavaScript
    Fetch API

Backend:
    Python 3.12
    FastAPI
    Uvicorn
    Requests
    BeautifulSoup

Servicios externos:
    Jikan API v4
    Wikipedia (scraping)

Instalación y Ejecución
[npm create vite@latest my-app -- --template react](https://react.dev/learn/installation)
🔹 Backend (FastAPI)
1. Crear entorno virtual
    python -m venv venv
    venv\Scripts\activate

2. Instalar dependencias
    pip install fastapi uvicorn requests beautifulsoup4

3. Ejecutar servidor
    uvicorn main:app --reload

🔹 Frontend (React + Vite)
1. Crear el proyecto React
    npm create vite@latest frontend

Seleccionar:

Framework: React
Variant: JavaScript

2. Instalar dependencias
    cd frontend
    npm install

3. Ejecutar la aplicación
    npm run dev

Imports Principales
    React
    import { useEffect, useState } from "react";

    FastAPI
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    
    API Jikan
    import requests

    Web Scraping 
    import requests
    from bs4 import BeautifulSoup

Uso de la API (Jikan)
    La aplicación utiliza Jikan API v4 para:
    Buscar animes
    Obtener personajes de un anime

Nota:
    Los personajes solo provienen de la API
    Se gestionan errores como:
    429 Too Many Requests
    504 Gateway Timeout

Web Scraping

    El scraping se realiza desde Wikipedia de forma responsable:
    URL: https://en.wikipedia.org/wiki/Category:Anime_series

CORS
    Se configura CORS en el backend para permitir la comunicación entre:
    Frontend (React – puerto 5173)
    Backend (FastAPI – puerto 8000)

Finalidad del Proyecto
    Este proyecto tiene un propósito educativo, enfocado en:
    Consumo de APIs REST
    Web scraping responsable
    Arquitectura frontend / backend
    Manejo de errores reales
    Buenas prácticas de desarrollo web