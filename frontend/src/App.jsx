// src/App.jsx
import React, { useState } from "react";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";
import AnimeCatalog from "./components/AnimeCatalog";

export default function App() {
  const [user, setUser] = useState(null);
  const [showRegister, setShowRegister] = useState(false);

  const handleLoginSuccess = (email) => setUser(email);
  const handleLogout = () => setUser(null);

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(-45deg, #ff758c, #ff7eb3, #6a82fb, #fc5c7d)",
      backgroundSize: "400% 400%",
      animation: "gradientBG 15s ease infinite",
      fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
      color: "#fff",
      transition: "all 0.3s ease",
      padding: "0 20px"
    }}>
      <nav style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "15px 0",
        backgroundColor: "rgba(0,0,0,0.3)",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 4px 15px rgba(0,0,0,0.3)"
      }}>
        <h1 style={{ margin: 0, fontSize: "1.8rem" }}>AnimeApp</h1>
        <div style={{ display: "flex", gap: "10px" }}>
          {user && (
            <button
              onClick={handleLogout}
              style={{
                padding: "8px 15px",
                borderRadius: "10px",
                border: "none",
                cursor: "pointer",
                background: "#e74c3c",
                fontWeight: "bold",
                color: "#fff",
                transition: "0.3s all",
              }}
              onMouseEnter={e => e.currentTarget.style.background = "#c0392b"}
              onMouseLeave={e => e.currentTarget.style.background = "#e74c3c"}
            >
              Cerrar Sesión
            </button>
          )}
        </div>
      </nav>

      {!user && !showRegister && (
        <LoginForm 
          onLoginSuccess={handleLoginSuccess} 
          switchToRegister={() => setShowRegister(true)} 
        />
      )}

      {!user && showRegister && (
        <RegisterForm switchToLogin={() => setShowRegister(false)} />
      )}

      {user && <AnimeCatalog />}

      <style>
        {`@keyframes gradientBG {
          0% {background-position: 0% 50%;}
          50% {background-position: 100% 50%;}
          100% {background-position: 0% 50%;}
        }`}
      </style>
    </div>
  );
}
