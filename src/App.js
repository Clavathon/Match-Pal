import React, { Component } from 'react';
import Login from './Login/Login';
import Registration from './Login/Registration';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Login></Login>
        {/* <Registration></Registration> */}
      </div>
    );
  }
}

export default App;
