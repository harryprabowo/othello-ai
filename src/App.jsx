import React, { useState } from 'react';
import './App.scss';

const App = () => {
  const [started, setStart] = useState(false)
  const [player, setPlayer] = useState(0)
  const [mode, setMode] = useState(0)
  const [difficulty, setDifficulty] = useState(1)
  const [turn, setTurn] = useState()
  const [board, setBoard] = useState()

  const sessionHandler = begin => {
    setTurn(begin ? player : null)
    setStart(begin)
  }

  const clickHandler = (row, col) => {
    console.log(row, col)
  }
  
  const move = (move, player) => {

  }

  const togglePlayer = () => setPlayer(!player)
  const toggleMode = () => setMode(!mode)
  const toggleDifficulty = diff => {
    const delta = (diff.deltaY * -1) > 0 ? 1 : -1
    setDifficulty(difficulty + delta > 3 || difficulty + delta < 1 ? difficulty : difficulty + delta)
  }

  return (
    <div id="container">
      <div id="start-modal" className= {started ? 'hide' : null}>
        <span onWheel={togglePlayer}>{!player ? <>be <label style={{ color: 'white', textShadow: "-1px -1px 0 #aaa, 1px -1px 0 #aaa, -1px 1px 0 #aaa, 1px 1px 0 #aaa" }}>white</label></> : <>be <label style={{ color: 'black' }}>black</label></>}</span>
        <span onWheel={toggleMode}>against {!mode ? <label style={{ color: 'red' }}>AI</label> : <label style={{ color: 'black' }}>people.</label>}</span>
        {
          !mode ? (
            <span onWheel={toggleDifficulty} style={{ color: 'black' }}>{difficulty === 1 ? `ez` : difficulty === 2 ? `hm` : `cry`}.</span>
          ) : null
        }
        <button className={"nav-btn right " + (started ? `hide` : null)} onClick={() => sessionHandler(true)}>→</button>
      </div>
      <button className={"nav-btn left " + (!started ? 'hide' : null)} onClick={() => sessionHandler(false)}>←</button>
      <div id="board" className={(!started ? 'hide' : "") + " " + (turn === player ? "" : 'turn')}>
        <span className={"score " + (!player ? `black` : `white`) + " " + "winning"} id="score-2">100</span>
        <table>
          <tbody>
            {
              [...Array(8)].map((e, i) => (
                <tr key={i}>
                  {
                    [...Array(8)].map((e, j) => (
                      <td className={`available`} key={j} onClick={() => clickHandler(j + 1, i + 1)}>
                        <label>{i === 0 || i === 7 ? j + 1 : (j === 0 ? i + 1 : null)}</label>
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                          <circle cx="50" cy="50" r="50" className={(j + (i % 2)) % 2 ? `black` : `white`} />
                        </svg>
                      </td>
                    ))
                  }
                </tr>
              ))
            }
          </tbody>
        </table>
        <span className={"score " + (player ? `black` : `white`) + " "} id="score-1">100</span>
      </div>
    </div>
  )
}

export default App;
