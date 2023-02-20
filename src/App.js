import logo from './logo.svg';
import './App.css';

import React, { useState } from "react";
import getAchievements from "./getAchievements";

function App() {
  const [achievements, setAchievements] = useState([]);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const lodestoneLink = document.getElementById("lodestone-link").value;
    try {
      const result = await getAchievements(lodestoneLink);
      setAchievements(result);
      setError("");
    } catch (error) {
      setError(error.message);
      setAchievements([]);
    }
  };

  return (
    <div>
      <h1>FFXIV Achievements</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="lodestone-link">Enter Lodestone Profile Link:</label>
        <input type="text" id="lodestone-link" />
        <button type="submit">Get Achievements</button>
      </form>
      {error && <div>{error}</div>}
      <ul>
      {achievements.map((achievement) => (
      <li key={achievement.ID}>
        {achievement.Name} - {achievement.Date}
      </li>
      ))}
      </ul>
    </div>
  );
}

export default App;