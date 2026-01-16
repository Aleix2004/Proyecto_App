// frontend/src/components/RegisterForm.jsx
import React, { useState } from "react";

export default function RegisterForm({ onRegisterSuccess, switchToLogin }) {
  const [nombre, setNombre] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fechaNacimiento, setFechaNacimiento] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setErrorMsg("");

    try {
      const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre, email, password, fecha_nacimiento: fechaNacimiento }),
      });

      if (!response.ok) {
        setErrorMsg("Error de conexión con el servidor");
        return;
      }

      const data = await response.json();

      if (!data.ok) {
        setErrorMsg(data.msg || "Error al registrar");
      } else {
        onRegisterSuccess(data.email);
      }
    } catch (error) {
      console.error("Error en fetch:", error);
      setErrorMsg("No se pudo conectar con el servidor");
    }
  };

  return (
    <div
      style={{
        maxWidth: "400px",
        margin: "0 auto",
        backgroundColor: "#fff",
        padding: "30px",
        borderRadius: "10px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
        color: "#333", // texto oscuro
      }}
    >
      <h2 style={{ textAlign: "center", marginBottom: "20px", color: "#007bff" }}>Registro</h2>
      <form onSubmit={handleRegister}>
        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>Nombre</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #ccc",
            }}
          />
        </div>
        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #ccc",
            }}
          />
        </div>
        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>Contraseña</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #ccc",
            }}
          />
        </div>
        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>Fecha de nacimiento</label>
          <input
            type="date"
            value={fechaNacimiento}
            onChange={(e) => setFechaNacimiento(e.target.value)}
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #ccc",
            }}
          />
        </div>
        {errorMsg && <p style={{ color: "red", marginBottom: "10px" }}>{errorMsg}</p>}
        <button
          type="submit"
          style={{
            width: "100%",
            padding: "12px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          Registrarse
        </button>
      </form>
      <p style={{ textAlign: "center", marginTop: "15px", color: "#333" }}>
        ¿Ya tienes cuenta?{" "}
        <span
          onClick={switchToLogin}
          style={{ color: "#007bff", cursor: "pointer", fontWeight: "bold" }}
        >
          Inicia sesión
        </span>
      </p>
    </div>
  );
}
