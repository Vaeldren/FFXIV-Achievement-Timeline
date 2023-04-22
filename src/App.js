import logo from './logo.svg';
import './App.css';

import React, { useState } from "react";
import getAchievements from "./getAchievements";

function App() {

  };
  

  return (
    <div>
      <h1>FFXIV Achievements</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="lodestone-link">Enter Lodestone Profile Link:</label>
        <input type="text" id="lodestone-link" />
        <button type="submit">Get Achievements</button>
      </form>
      
      

    </div>
  );


export default App;