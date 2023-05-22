import React, { useState } from "react"; 
import logo from './HearMeOut-1.png';
import './App.css';
import { Login } from "./Login";
import { Register } from "./Register";

function App() {
  const [currentForm, setCurrentForm] = useState('login');
  const toggleForm = (formName) => {
    setCurrentForm(formName); 
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <Register onFormSwitch={toggleForm} />
      }
        <p>
           <code> Convert from Text to Speech </code> 
           <p> With a click of a button </p>
           <input type="text" />
           <button>Convert</button>
        </p>
        <a
          className="App-link"
          href="https://github.com/YZDavid/HearMeOut"
          target="_blank"
          rel="noopener noreferrer"
        >
          About Our Project
        </a>
        <h2> 📝 🎧 </h2> 
      </header>
    </div>
  );
}

export default App;