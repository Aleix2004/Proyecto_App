import React, { useEffect, useState } from "react";
import Personajes from "./Personajes";

// Diccionario de imágenes de animes
const animeImages = {
  "Chainsaw Man": "https://cdn.myanimelist.net/images/anime/1806/126216.jpg",
  "Sousou no Frieren": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
  "Fullmetal Alchemist: Brotherhood": "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
  "Steins;Gate": "https://cdn.myanimelist.net/images/anime/5/73199.jpg",
  "Shingeki no Kyojin Season 3 Part 2": "https://cdn.myanimelist.net/images/anime/1517/100633.jpg",
  "Gintama°": "https://cdn.myanimelist.net/images/anime/3/72078.jpg",
  "Hunter x Hunter (2011)": "https://cdn.myanimelist.net/images/anime/1337/99013.jpg",
  "One Piece": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
};

// Map de nombres “tarjeta” → nombres para Jikan API
const animeNameMap = {
  "Chainsaw Man": "Chainsaw Man",
  "Sousou no Frieren": "Sousou no Frieren",
  "Fullmetal Alchemist: Brotherhood": "Fullmetal Alchemist: Brotherhood",
  "Steins;Gate": "Steins;Gate",
  "Shingeki no Kyojin Season 3 Part 2": "Shingeki no Kyojin",
  "Gintama°": "Gintama",
  "Hunter x Hunter (2011)": "Hunter x Hunter (2011)",
  "One Piece": "One Piece",
};

const placeholderImg = "https://via.placeholder.com/150x220?text=Anime";

export default function AnimeCatalog() {
  const [animes, setAnimes] = useState([]);
  const [selectedAnime, setSelectedAnime] = useState(null);
  const [jikanName, setJikanName] = useState(null); // Nombre real para Jikan

  useEffect(() => {
    fetch("http://127.0.0.1:8000/animes-populares")
      .then((res) => res.json())
      .then((data) => {
        if (data.ok) setAnimes(data.animes);
      })
      .catch((err) => console.error("Error al cargar animes:", err));
  }, []);

  const handleVerPersonajes = (anime) => {
    setSelectedAnime(anime);
    setJikanName(animeNameMap[anime] || anime); // Tomamos nombre para Jikan
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial, sans-serif" }}>
      <h2 style={{ color: "#222", marginBottom: "20px" }}>🎌 Animes Populares</h2>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "24px",
        }}
      >
        {animes.map((anime) => (
          <div
            key={anime}
            style={{
              width: "180px",
              backgroundColor: "#1f2933",
              borderRadius: "16px",
              padding: "14px",
              textAlign: "center",
              boxShadow: "0 6px 15px rgba(0,0,0,0.25)",
            }}
          >
            <img
              src={animeImages[anime] || placeholderImg}
              alt={anime}
              style={{
                width: "100%",
                maxWidth: "140px",
                height: "200px",
                objectFit: "cover",
                borderRadius: "12px",
                margin: "0 auto",
                display: "block",
              }}
            />

            <h4
              style={{
                fontSize: "14px",
                margin: "12px 0",
                color: "#fff",
                minHeight: "38px",
              }}
            >
              {anime}
            </h4>

            <button
              onClick={() => handleVerPersonajes(anime)}
              style={{
                backgroundColor: "#22c55e",
                color: "#000",
                border: "none",
                padding: "6px 12px",
                borderRadius: "8px",
                cursor: "pointer",
                fontSize: "12px",
                fontWeight: "bold",
              }}
            >
              Ver Personajes
            </button>
          </div>
        ))}
      </div>

      {selectedAnime && jikanName && (
        <div style={{ marginTop: "50px" }}>
          <h3 style={{ color: "#222", marginBottom: "20px" }}>
            👥 Personajes de {selectedAnime}
          </h3>
          <Personajes nombreAnime={jikanName} />
        </div>
      )}
    </div>
  );
}
