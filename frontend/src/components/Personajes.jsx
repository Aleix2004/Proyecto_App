// src/components/Personajes.jsx
import React, { useEffect, useState } from "react";

export default function Personajes({ nombreAnime }) {
  const [personajes, setPersonajes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch(`http://127.0.0.1:8000/personajes?nombre_anime=${encodeURIComponent(nombreAnime)}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.ok) setPersonajes(data.personajes);
        else setPersonajes([]);
      })
      .catch(() => setPersonajes([]))
      .finally(() => setLoading(false));
  }, [nombreAnime]);

  if (loading) return <p style={{ textAlign: "center" }}>Cargando personajes...</p>;
  if (!personajes || personajes.length === 0) return <p style={{ textAlign: "center" }}>No hay personajes</p>;

  return (
    <div style={{
      display: "flex",
      flexDirection: "column", // Mostramos en columna
      gap: "10px",
      padding: "10px",
      marginTop: "10px",
    }}>
      {personajes.map((p, idx) => (
        <div key={idx} style={{
          borderRadius: "12px",
          background: "linear-gradient(135deg, #6a82fb, #fc5c7d)",
          padding: "10px",
          color: "#fff",
          fontWeight: "bold",
          textAlign: "center",
          boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
          transition: "transform 0.2s"
        }}
        onMouseEnter={e => e.currentTarget.style.transform = "scale(1.05)"}
        onMouseLeave={e => e.currentTarget.style.transform = "scale(1)"}
        >
          {p}
        </div>
      ))}
    </div>
  );
}
