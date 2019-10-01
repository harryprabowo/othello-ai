import constant
import math
from board import *


class Bot:
    def __init__(self, board, piece_color):
        self.board = board
        self.piece_color = piece_color
        self.depth = constant.DEFAULT_DEPTH

    def move(self, current_state):
        return self.dfs(current_state, self.piece_color, self.depth, -math.inf, math.inf)

    def dfs(self, current_state, current_player, remaining_depth, alpha, beta):
        if remaining_depth == 0:
            return self.__evaluate_state(current_state), None
        else:
            possible_step = self.board.possible_moves(current_player)
            if not possible_step:
                if not self.board.possible_moves(self.__enemy_of(current_player)):
                    return self.__final_value(current_state), None
                else:
                    return -self.dfs(current_state, self.__enemy_of(current_player), remaining_depth - 1, -beta, -alpha)[0], None
            best_value = -999 if (self.piece_color == current_player) else 999
            best_move = 0
            for step in possible_step:
                next_board = Board(current_state)
                next_board.make_move(step, current_player)
                next_state = next_board.get_state()
                value = -self.dfs(next_state, self.__enemy_of(current_player), remaining_depth - 1, -beta, -alpha)[0]
                if current_player == self.piece_color:
                    if best_value < value:
                        best_value = value
                        alpha = value
                        best_move = step
                else:
                    if best_value > value:
                        best_value = value
                        beta = value
                        best_move = step
                if beta <= alpha:
                    break
            return best_value, best_move

    def __final_value(self, state):
        score = self.__score(state)
        if score < 0:
            return constant.MIN_VALUE
        elif score > 0:
            return constant.MAX_VALUE
        else:
            return score

    def __score(self, state):
        return state.count(self.piece_color) - state.count(self.__enemy_of(self.piece_color))

    def __square_list(self):
        return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

    def __evaluate_state(self, state):
        res = 0
        for square in self.__square_list():
            modifier = 1 if (state[square] == self.piece_color) else -1
            res += constant.BOARD_VALUE[square] * modifier
        return res

    def __enemy_of(self, current_player):
        if current_player == constant.WHITE:
            return constant.BLACK
        else:
            return constant.WHITE
