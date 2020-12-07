import React, { Fragment, useState} from 'react';
import './App.css';
import axios from "axios"

//import component
import invaderGameList from "./components/invaderGameList"

// const click = () => {
//   console.log("hello");
// } 

    // リストの状態
    // const [scores, setScores] = useState([]);

const clickUsual = async()=> {
  try {
    console.log("ttttttt");
      const response = await fetch("http://localhost:5000/scores");
      // const response = axios.get("/scores");
　　　　　　 const jsonData = await response.json();　
      console.log(jsonData);
      // setScores(jsonData);
  } catch (error) {
      console.error(error.message);
  }
}

const clickNiece = async()=> {
  try {
    console.log("sssssss");
      // const response = await fetch("http://localhost:5000/scores");
      const response = await fetch("/scores");
　　　　　　 const jsonData = await response.json();　
      console.log(jsonData);
      // setScores(jsonData);
  } catch (error) {
      console.error(error.message);
  }
}


function App() {
  return (
    <Fragment>
      <div className="container">
        <h1>Space Invader</h1>
        <button onClick={clickUsual}>game</button>
        <button onClick={clickNiece}>game for Niece</button>
        {/* <a href="https://www.yahoo.co.jp/" >yahoo</a> */}
        <invaderGameList />
      </div>
    </Fragment>
  );
}

export default App;
