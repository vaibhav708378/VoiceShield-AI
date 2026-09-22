import { useState } from "react";
import API from "../services/api";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await API.post("/auth/login", {
        email: email,
        password: password,
      });

      const token = response.data.access_token;

      localStorage.setItem("access_token", token);

      setMessage("Login successful!");

      console.log("JWT Token:", token);

    } catch (error) {
      console.error(error);

      setMessage(
        error.response?.data?.detail || "Login failed"
      );
    }
  };

  return (
    <div>
      <h1>VoiceShield AI</h1>

      <h2>Login</h2>

      <form onSubmit={handleLogin}>

        <div>
          <label>Email</label>
          <br />

          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
          />
        </div>

        <br />

        <div>
          <label>Password</label>
          <br />

          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
          />
        </div>

        <br />

        <button type="submit">
          Login
        </button>

      </form>

      <p>{message}</p>
    </div>
  );
}

export default Login;