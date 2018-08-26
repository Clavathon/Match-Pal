import React, { Component } from 'react'
import Login from './Login/Login'
import Routes from './Routes/Routes'

class App extends Component {
  render() {
    return (
      <div className="App">
        <Routes></Routes>
        <h1>
            This is located in app.js
            For interesting shenanigans, use url `/user/[some name string]` to add stuff into db

        </h1>
        <br/>
        <h1>
            Use `/user` to retrieve all users from the database
        </h1>

      </div>
    );
  }
}

export default App;
