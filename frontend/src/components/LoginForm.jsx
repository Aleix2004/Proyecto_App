// src/components/LoginForm.jsx
import React, { useState } from "react";

export default function LoginForm({ onLoginSuccess, switchToRegister }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMsg("");
    try {
      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      if (!data.ok) setErrorMsg(data.msg);
      else onLoginSuccess(data.email);
    } catch (err) {
      setErrorMsg("Error al conectar con el servidor");
    }
  };

  return (
    <div style={{
      maxWidth: "400px",
      margin: "50px auto",
      padding: "30px",
      borderRadius: "12px",
      background: "rgba(0,0,0,0.4)",
      boxShadow: "0 4px 20px rgba(0,0,0,0.5)",
      textAlign: "center",
      color: "#fff"
    }}>
      <h2 style={{ marginBottom: "20px", fontSize: "1.8rem" }}>Login</h2>
      <form onSubmit={handleLogin}>
        <input 
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
          style={inputStyle}
        />
        <input 
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
          style={inputStyle}
        />
        {errorMsg && <p style={{ color: "#e74c3c" }}>{errorMsg}</p>}
        <button type="submit" style={buttonStyle}>Iniciar Sesión</button>
      </form>
      <p style={{ marginTop: "15px" }}>
        ¿No tienes cuenta? <span onClick={switchToRegister} style={{ color: "#f1c40f", cursor: "pointer" }}>Regístrate</span>
      </p>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "12px",
  margin: "10px 0",
  borderRadius: "8px",
  border: "none",
  fontSize: "1rem"
};

const buttonStyle = {
  width: "100%",
  padding: "12px",
  marginTop: "15px",
  borderRadius: "10px",
  border: "none",
  fontSize: "1rem",
  fontWeight: "bold",
  background: "linear-gradient(90deg, #f12711, #f5af19)",
  color: "#fff",
  cursor: "pointer",
  transition: "transform 0.2s",
};
