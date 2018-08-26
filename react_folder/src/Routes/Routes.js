import React from 'react'
import {
  BrowserRouter as 
  Router,
  Route,
  Switch
} from 'react-router-dom'
import Login from '../Login/Login'
import Registration from '../Login/Registration'

class Routes extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path='/' component={Login} />
          <Route path='/registration' component={Registration} />
        </Switch>
      </Router>
    )
  }
}

export default Routes;