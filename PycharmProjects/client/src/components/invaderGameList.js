import React, { Fragment, useEffect, useState} from "react";
// import main from "../../main.py"

const InvaderGamelList = () => {

    // リストの状態
    const [scores, setScores] = useState([]);


    //scoresを追加する。
    // const create = async e => {
    //     try {
    //         const body = { point };
    //         const response = await fetch("http://localhost:5000/scores", {
    //             method : "POST",
    //             headers : {"Content-Type" : "application/json" },
    //             body : JSON.stringify(body)
    //         })
    //     } catch (error) {
    //         console.error(error.message);
    //     }
    // }


　  //とにかくゲットする
    // useEffect(() => {
        const getScores = async()=> {
            try {
                const response = await fetch("http://localhost:5000/scores");
    　　　　　　 const jsonData = await response.json();　
                console.log(jsonData);
                setScores(jsonData);
            } catch (error) {
                console.error(error.message);
            }
        }

        getScores();

        
    // },[])


    return (
    <Fragment>
        <h1 className="text-center mt-5">Invader Game</h1>
    </Fragment>
    );
};

export default InvaderGamelList