import './App.css';
import React, { useState } from "react";
import Timeline from './Timeline'
import './Title.css';

function Title(){
  return (
    <div  className = "Title">
      <h1>Final Fantasy XIV Achievement Timeline</h1>
    </div>
  )
}


function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [isError, setError] = useState(null);
  const [results, setResults] = useState(null);
  const [link, setLink] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setError(false);
    try {
      const response = await fetch('http://127.0.0.1:5000/api/get', {
        method: 'GET'
      });
      const result = await response.json();
      setResults(result);
      setIsLoading(false);
      setError(false);
    } catch (error) {
      setIsLoading(false);
      setError(true)
      if("TypeError:" in error){
      setError("Profile private. Please make your achievements public on your Lodestone.");
      }
      else{
      setError("URL error. Please double-check that the URL you are entering is to your Lodestone profile.");
      }


      //handle error
      console.log(error);
    }

  }

  const handleLinkChange = (event) => {
    setLink(event.target.value);
  }

  return (
    <div className='bgcolor'>
      <Title/>
      <div className='Body'>
      <form onSubmit={handleSubmit}>
        <label htmlFor="lodestone-link">Enter Lodestone Profile Link: </label>
        <input type="text" id="lodestone-link" className='textboxid' value={link} onChange={handleLinkChange} />
        <p></p>
        <button type="submit">Get Achievements</button>
        <p></p>
        {isLoading && !isError && <a>Loading...</a>}
      {isError && !isLoading && <a>{isError}</a>}
      {!isLoading && results && <Timeline achievements={results}/>}
      </form>
      </div>
    </div>
  );
};

export default App;
