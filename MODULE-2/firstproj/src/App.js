// import logo from './logo.svg';
import './App.css';
import Users from './Users/Users.js';
import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  // Redirect,
  Switch
} from 'react-router-dom';
// import Banners from './Users/Banners.js'

function App() {
  return (
    // <div className="App">
    //   <header className="App-Header">
        
    //   </header>
    // </div>
    <Router>
      <Switch>
        <Route path="/form" exact>
          <Users />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;

// import './App.css';
// import Users from './Users/Banners.js';
// import Header from './components/Header.js';
// import Body from './components/Body.js';
// import Footer from './components/Footer.js';
// import React from 'react';
// import interest_calculator from './Users/interest_calclulator.js';

// function App() {
//   return (
//     // <div className="App">
//     //   <header className="App-header">
//     //     <Header/>
//     //     <Body/>
//     //    <Footer/>
//     //   </header>
//     // </div>
    
//   );
// }
// export default App;