// src/api.js
const BASE_URL = "http://127.0.0.1:8000";

export async function loginUser(email, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
}

export async function registerUser(nombre, email, password, fecha_nacimiento) {
  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, email, password, fecha_nacimiento }),
  });
  return res.json();
}

export async function getAnimesPopulares() {
  const res = await fetch(`${BASE_URL}/animes-populares`);
  return res.json();
}

export async function getPersonajes(nombre_anime) {
  const res = await fetch(`${BASE_URL}/personajes?nombre_anime=${encodeURIComponent(nombre_anime)}`);
  return res.json();
}
