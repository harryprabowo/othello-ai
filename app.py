from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from bot import *
from board import *
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
board = None
bot = None
mode = 0
ai = 0


def update_board_by_bot(current_player):
    global board, mode
    if mode == 1:
        bot_move = move_bot(current_player)
        board.make_move(bot_move, current_player)
        return enemy_of(current_player)
    else:
        return current_player


def move_bot(current_player):
    global ai, bot
    if ai == 0:
        return random.choice(board.possible_moves(current_player))
    else:
        return bot.move(board.get_state())[1]

@app.route('/', methods=['POST'])
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/api/move', methods=['POST'])
@cross_origin()
def api():
    global board
    current_player = int(request.json['player'])
    player_move = int(request.json['move'])
    if player_move is not None:
        board.make_move(player_move, current_player)
        current_player = enemy_of(current_player)
    current_player = update_board_by_bot(current_player)
    return jsonify(state=board.get_state(), possible_move=board.possible_moves(current_player))


@app.route('/api/start', methods=['POST'])
@cross_origin()
def start():
    global board, bot, mode, ai, DEFAULT_DEPTH
    board = Board()
    current_player = int(request.json['player'])
    mode = int(request.json['mode'])
    ai = int(request.json['ai'])
    difficulty = int(request.json['difficulty'])
    if difficulty is not None:
        bot = Bot(board, enemy_of(current_player), difficulty*2)
    else:
        bot = Bot(board, enemy_of(current_player))
    if current_player == constant.WHITE:
        current_player = update_board_by_bot(current_player)
    return jsonify(state=board.get_state(), possible_move=board.possible_moves(current_player))


if __name__ == '__main__':
    app.run(port=8080)
