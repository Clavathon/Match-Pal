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
import Upload from '../Upload/Upload';

class Routes extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path='/' component={Search} />
          <Route path='/login' component={Login} />
          <Route path='/registration' component={Registration} />
          <Route path='/search' component={Search} />
          <Route path='/upload' component={Upload} />
        </Switch>
      </Router>
    )
  }
}

export default Routes;