// Pages 
import Home from './pages/Home';
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";


// Styled Components 
import { StyledContainer } from './components/Styles';

import React from 'react';

//Loader css 
import {
    BrowserRouter as Router, Switch, Route
} from 'react-router-dom';


function App() {
    return (
      <Router>
        <StyledContainer>
          <Switch>
            <Route path="/signup">
              <Signup />
            </Route>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/dashboard">
              <Dashboard />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </StyledContainer>
      </Router>
    );
}

export default App; 
