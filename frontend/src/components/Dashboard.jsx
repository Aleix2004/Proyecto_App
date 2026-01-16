import React, { useState } from "react";
import AnimeList from "./AnimeList";
import Personajes from "./Personajes";

export default function Dashboard({ userEmail, onLogout }) {
  const [selectedAnimeId, setSelectedAnimeId] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Bienvenido, {userEmail}</h2>
      <button onClick={onLogout}>Cerrar Sesión</button>

      <hr />

      <h3>Animes Populares</h3>
      <AnimeList onSelectAnime={(id) => setSelectedAnimeId(id)} />

      {selectedAnimeId && (
        <>
          <hr />
          <h3>Personajes del Anime</h3>
          <Personajes animeId={selectedAnimeId} />
        </>
      )}
    </div>
  );
}
