import './App.css';
import React, { useState } from "react";
import Timeline from './Timeline'

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [link, setLink] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const response = await fetch('/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          link: link
        })
      });
      const result = await response.json();
      setResults(result);
      setIsLoading(false);
    } catch (error) {
      setIsLoading(false);
      //handle error
      console.error(error);
      console.log(error);
    }
  }

  const handleLinkChange = (event) => {
    setLink(event.target.value);
  }

  return (
    <div>
      <h1>FFXIV Achievements</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="lodestone-link">Enter Lodestone Profile Link:</label>
        <input type="text" id="lodestone-link" value={link} onChange={handleLinkChange} />
        <button type="submit">Get Achievements</button>
      </form>
      {isLoading && <p>Loading...</p>}
      {!isLoading && results && <Timeline achievements={results}/>}
    </div>
  );
};

export default App;
