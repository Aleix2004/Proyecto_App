import React, { useEffect, useState } from "react";

export default function PopularAnimes() {
  const [animes, setAnimes] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/animes-populares")
      .then((res) => res.json())
      .then((data) => data.ok && setAnimes(data.animes))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Animes Populares</h2>
      <ul>
        {animes.map((a, i) => (
          <li key={i}>{a.title || a}</li>
        ))}
      </ul>
    </div>
  );
}
