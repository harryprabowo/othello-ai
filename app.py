from flask import Flask, jsonify, request
from bot import *
from board import *

app = Flask(__name__)
board = None
bot = None
mode = 0
ai = 0


@app.route('/api/move', methods=['POST'])
def api():
    current_player = request.form.get('player')
    player_move = request.form.get('move')
    if player_move is not None:
        board.make_move(player_move, current_player)
    bot_move = bot.move(board.get_state())[1]
    board.make_move(bot_move, current_player)
    return jsonify(state=board.get_state(), possible_move=board.possible_moves(current_player))


@app.route('/api/start', methods=['POST'])
def start():
    global board, bot, mode, ai
    board = Board()
    human_player = int(request.json['player'])
    mode = request.form.get('mode')
    ai = request.form.get('ai')
    bot = Bot(board, enemy_of(human_player))
    print(board.get_state())
    return jsonify(state=board.get_state(), possible_move=board.possible_moves(human_player))


if __name__ == '__main__':
    app.run(port=8080)
