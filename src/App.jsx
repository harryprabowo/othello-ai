import React, { useState } from 'react';
import './App.scss';
import { isNullOrUndefined } from 'util';

const API_URL = `http://localhost:8080/api/`

const App = () => {
  const [started, setStart] = useState(false)
  const [player, setPlayer] = useState(0)
  const [mode, setMode] = useState(0)
  const [ai, setAi] = useState(1)
  const [difficulty, setDifficulty] = useState(1)
  const [turn, setTurn] = useState(player)
  const [allowedMoves, setAllowedMoves] = useState([])
  const [board, setBoard] = useState()
  const [scoreBlack, setScoreBlack] = useState(0)
  const [scoreWhite, setScoreWhite] = useState(0)

  const sessionHandler = begin => {
    if (begin) {
      player ? setTurn(!player ? 1 : 0) : setTurn(player)
      const params = {
        mode: mode + 1,
        ai: ai,
        player: player + 1,
        difficulty: difficulty
      }

      fetch(API_URL + `start`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(params)
      })
        .then(res => res.json())
        .then(data => {
          setAllowedMoves(data.possible_move)
          setBoard(data.state)
          countScore(data.state)
        })
        .catch(e => {
          console.error(e)
        })
    } else {
      setScoreBlack(0)
      setScoreWhite(0)
      setTurn(null)
      setAllowedMoves([])
      setBoard(null)
    }

    setStart(begin)
  }

  const countScore = (state = board) => {
    const occurence = state.reduce((acc, curr) => {
      acc[curr] ? acc[curr]++ : acc[curr] = 1

      return acc
    }, {})

    setScoreBlack(occurence[2])
    setScoreWhite(occurence[1])
  }

  const moveTo = move => {
    const params = {
      move: move,
      player: turn + 1
    }

    fetch(API_URL + `move`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params)
    })
      .then(res => res.json())
      .then(data => {
        if (data.possible_move.length === 0) {
          if(scoreWhite === scoreBlack) alert(`What! A tie!?`)
          else (scoreWhite > scoreBlack ? !player : player) ? alert(`You have skills.`) :  alert('Too bad.')
          setAllowedMoves(data.possible_move)
          setBoard(data.state)
          if (mode === 1) setTurn(!turn ? 1 : 0)
          countScore(data.state)
        } else {
          setAllowedMoves(data.possible_move)
          setBoard(data.state)
          if (mode === 1) setTurn(!turn ? 1 : 0)
          countScore(data.state)
        }
      })
      .catch(e => {
        console.error(e)
      })
  }

  const pieceColor = num => {
    if (num === 1)
      return player ? 'white' : 'black'
    else if (num === 2)
      return player ? 'black' : 'white'
    else if (num === 3)
      return null
    else return ""
  }

  const score = color => {
    if(color === 'black') {
      return (scoreBlack > scoreWhite ? <strong>{scoreBlack}</strong> : scoreBlack)
    } else {
      return (scoreWhite > scoreBlack ? <strong>{scoreWhite}</strong> : scoreWhite)
    }
  }

  const togglePlayer = () => setPlayer(!player)
  const toggleMode = diff => {
    let delta = diff.deltaY > 0 ? 1 : -1

    if(mode) { // pvp 2
      if(delta < 0) setMode(mode + delta)
    } else { // AI 1
      if(!ai) delta > 0 ? setMode(mode + delta) : setAi(ai - delta) 
      else {
        if(delta > 0) setAi(ai - delta)
      }
    }
  }
  const toggleDifficulty = diff => {
    let delta = (diff.deltaY * -1) > 0 ? 1 : -1
    setDifficulty(difficulty + delta > 3 || difficulty + delta < 1 ? difficulty : difficulty + delta)
  }

  return (
    <div id="container">
      <div id="start-modal" className={started ? 'hide' : null}>
        <span onWheel={togglePlayer} onClick={togglePlayer}>{player ? <>be <label style={{ color: 'white', textShadow: "-1px -1px 0 #aaa, 1px -1px 0 #aaa, -1px 1px 0 #aaa, 1px 1px 0 #aaa" }}>white</label></> : <>be <label style={{ color: 'black' }}>black</label></>}</span>
        <br className="responsive-br"/>
        <span onWheel={toggleMode} onClick={toggleMode}>against {!mode ? <label style={{ color: 'red' }}>{ai ? `AI` : 'random'}</label> : <label style={{ color: 'black' }}>people.</label>}</span>
        <br className="responsive-br"/>
        {
          !mode && ai ? (
            <span onWheel={toggleDifficulty} onClick={toggleDifficulty}style={{ color: 'black' }}>{difficulty === 1 ? `ez` : difficulty === 2 ? `hm` : `cry`}.</span>
          ) : null
        }
        <button className={"nav-btn right " + (started ? `hide` : null)} onClick={() => sessionHandler(true)}>→</button>
      </div>
      <button 
      className={"nav-btn left " + (!started ? 'hide' : null)} 
      onClick={() => {if(window.confirm(`Are you sure you want to end the game?`)) sessionHandler(false)}}>
        ←
      </button>
      <div id="board" className={(!started ? 'hide ' : "") + (turn ? "" : 'turn')}>
        <span className={"score " + (!player ? `black` : `white`)} id="score-2">{score(!player ? `black` : `white`)}</span>
        <table>
          <tbody>
            {
              [...Array(8)].map((e, i) => (
                <tr key={i}>
                  {
                    [...Array(8)].map((e, j) => (
                      <td className={!allowedMoves.includes((j + 1) * 10 + i + 1) ? `unavailable` : ''} key={j} onClick={() => moveTo((j + 1) * 10 + i + 1)}>
                        <label>{i === 0 || i === 7 ? j + 1 : (j === 0 ? i + 1 : null)}</label>
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                          <circle cx="50" cy="50" r="50" className={isNullOrUndefined(board) ? "" : pieceColor(board[(j + 1) * 10 + i + 1])} />
                        </svg>
                      </td>
                    ))
                  }
                </tr>
              ))
            }
          </tbody>
        </table>
        <span className={"score " + (player ? `black` : `white`) + " "} id="score-1">{score(player ? `black` : `white`)}</span>
      </div>
      <span className=""></span>
    </div>
  )
}

export default App;
