from flask import Flask, jsonify
from bot import *
from board import *

app = Flask(__name__)


@app.route('/api')
def hello():
    board = Board()
    bot = Bot(board, constant.BLACK)
    current_player = constant.BLACK
    bot_move = bot.move(board.get_state())[1]
    board.make_move(bot_move, current_player)
    return jsonify([board.get_state(), board.possible_moves(current_player)])


if __name__ == '__main__':
    app.run(port=8080)
