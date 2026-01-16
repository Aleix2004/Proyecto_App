// src/components/AnimeList.jsx
import React, { useEffect, useState } from "react";
import Personajes from "./Personajes";

export default function AnimeList() {
  const [animes, setAnimes] = useState([]);
  const [personajes, setPersonajes] = useState([]);
  const [selectedAnime, setSelectedAnime] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/animes-populares")
      .then(res => res.json())
      .then(data => setAnimes(data.animes || []))
      .catch(err => console.error(err));
  }, []);

  const handleClick = async (anime) => {
    setSelectedAnime(anime);
    setLoading(true);
    setPersonajes([]);
    try {
      const res = await fetch(`http://127.0.0.1:8000/personajes?nombre_anime=${anime.toLowerCase()}`);
      const data = await res.json();
      setPersonajes(data.personajes || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2 style={{ textAlign: "center", fontSize: "1.8rem", marginBottom: "15px" }}>Animes Populares</h2>
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "15px" }}>
        {animes.map((anime, idx) => (
          <button 
            key={idx}
            onClick={() => handleClick(anime)}
            style={{
              padding: "12px 20px",
              borderRadius: "12px",
              border: "none",
              cursor: "pointer",
              background: "#6a82fb",
              color: "#fff",
              fontWeight: "bold",
              boxShadow: "0 4px 15px rgba(0,0,0,0.3)",
              transition: "all 0.3s",
            }}
            onMouseEnter={e => e.currentTarget.style.transform = "scale(1.05)"}
            onMouseLeave={e => e.currentTarget.style.transform = "scale(1)"}
          >
            {anime}
          </button>
        ))}
      </div>

      {selectedAnime && (
        <div style={{ marginTop: "30px" }}>
          <h3 style={{ textAlign: "center", fontSize: "1.5rem" }}>{selectedAnime}</h3>
          <Personajes personajes={personajes} loading={loading} />
        </div>
      )}
    </div>
  );
}
