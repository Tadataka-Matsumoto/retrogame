import React, { Fragment } from 'react';
import './App.css';

//import component
import invaderGameList from "./components/invaderGameList"

// const click = () => {
//   console.log("hello");
// } 

function App() {
  return (
    // <Fragment>
      <div className="container">
        <h1>古いゲーム</h1>
        <h2>新しいゲーム</h2>
        <a href="https://www.yahoo.co.jp/" >yahoo</a>
        <invaderGameList />
      </div>
    // </Fragment>
  );
}

export default App;
