import { useEffect, useState } from "react";
import API from "../services/api";
import AudioMonitor from "./AudioMonitor";

function Dashboard() {
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      setMessage("You are not logged in.");
      return;
    }

    API.get("/auth/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => {
        setUser(response.data);
        setMessage("");
      })
      .catch((error) => {
        console.error(error);
        setMessage("Session expired. Please login again.");
        localStorage.removeItem("access_token");
      });
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    window.location.reload();
  };

  if (message) {
    return <h2>{message}</h2>;
  }

  return (
    <div>
      <h1>VoiceShield AI</h1>

      <h2>Dashboard</h2>

      {user && (
        <div>
          <h3>Welcome, {user.name} 👋</h3>

          <p>
            <strong>Email:</strong> {user.email}
          </p>

          <p>
            <strong>User ID:</strong> {user.id}
          </p>

          <p>
            <strong>Account Created:</strong>{" "}
            {new Date(user.created_at).toLocaleString()}
          </p>
        </div>
      )}

      <hr />

      <h2><AudioMonitor /></h2>

      <p>
        VoiceShield AI will analyze voice calls for:
      </p>

      <ul>
        <li>🎙️ Speaker verification</li>
        <li>🤖 AI-generated voice detection</li>
        <li>🚨 Scam detection</li>
        <li>🛡️ Risk analysis</li>
      </ul>

      <button onClick={handleLogout}>
        Logout
      </button>
    </div>
  );
}

export default Dashboard;