import React, { useState } from "react"; 
import logo from './HearMeOut-1.png';
import './App.css';
import { Login } from "./Login";
import { Register } from "./Register";
// import { Routes, Route, useNavigate } from "react-router-dom";
import { StyledContainer } from "./Components/Styles";

import Home from './Components/Styles/Home'

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
        <a
          className="App-link"
          href="https://github.com/YZDavid/HearMeOut"
          target="_blank"
          rel="noopener noreferrer"
        >
        <h4>About Our Project</h4>
        </a>
        <h6> 📝 🎧 </h6> 
      </header>
    </div>
  );
}

export default App;