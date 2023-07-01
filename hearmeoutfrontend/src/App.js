// Pages 
import Home from './pages/Home';
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import Convert from "./pages/Convert";


// Styled Components 
import { StyledContainer } from './components/Styles';

import React from 'react';

//Loader css 
import {
    BrowserRouter as Router, Switch, Route
} from 'react-router-dom';

// auth & redux
import AuthRoute from "./components/AuthRoute";
import BasicRoute from "./components/BasicRoute";
import { connect } from "react-redux";

function App() {
    return (
      <Router>
        <StyledContainer>
          <Switch>
            <Route path="/signup">
              <Signup />
            </Route>
            <Route path="/convert">
              <Convert />
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
