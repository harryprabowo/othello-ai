from flask import Flask, jsonify
from bot import *
from board import *

app = Flask(__name__)


@app.route('/')
def hello():
    board = Board()
    bot = Bot(constant.WHITE)
    state = board.get_state()
    return jsonify(state)

if __name__ == '__main__':
    app.run(port=8080)
