import React from 'react'
import {
  BrowserRouter as 
  Router,
  Route,
  Switch
} from 'react-router-dom'
import Search from '../Search/Search'
import Login from '../Login/Login'
import Registration from '../Login/Registration'

class Routes extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path='/' component={Search} />
          <Route path='/login' component={Login} />
          <Route path='/registration' component={Registration} />
          <Route path='/search' component={Search} />
        </Switch>
      </Router>
    )
  }
}

export default Routes;