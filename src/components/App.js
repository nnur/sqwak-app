import React, { Component } from 'react';
import { Router, Route, browserHistory } from 'react-router';
import LandingPage from './pages/Landing';
import LoginPage from './pages/Login';
import ModalManager from './pages/ModalManager';
import WarningManager from './pages/WarningManager';
import DashboardPage from './pages/dashboard/Dashboard';
import MlAppsPage from './pages/mlApps/MlAppsPage';
import NotFoundPage from './pages/NotFound';
import { requireAuth } from './../services/auth';


class App extends Component {

  render() {
    return (
      <div className="sq-full-page">
        <WarningManager />
        <ModalManager />
        <Router history={browserHistory}>
          <Route path="/" component={LandingPage}/>
          <Route path="/login" component={() => (<LoginPage isLogin={true} action={"Log In"} />)}/>
          <Route path="/signup" component={() => (<LoginPage action={"Sign Up"} />)}/>
          <Route path="/user/:userId/apps/:appId/dashboard" component={DashboardPage} onEnter={requireAuth}/>
          <Route path="/user/:userId/apps" component={MlAppsPage} onEnter={requireAuth}/>
          <Route path="*" component={NotFoundPage} />
        </Router>
      </div>
    );
  }
}

export default App