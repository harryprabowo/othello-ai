import constant
import math


class Bot:
    def __init__(self, piece_color):
        self.piece_color = piece_color
        self.depth = constant.DEFAULTDEPTH

    def move(self, current_state):
        return self.dfs(current_state, self.piece_color, self.depth, -math.inf, math.inf)

    def dfs(self, current_state, current_player, remaining_depth, alpha, beta):
        if remaining_depth == 0:
            return self.__evaluate_state(current_state)
        else:
            possible_step = self.__generate_possible_step(current_state, current_player)
            best_value = -999 if (self.piece_color == current_player) else 999
            for step in possible_step:
                next_state = self.__change_state(step, current_state)
                value = self.dfs(next_state, self.__enemy_of(current_player), remaining_depth - 1, alpha, beta)
                if current_player == self.piece_color:
                    best_value = max(best_value, value)
                    alpha = max(alpha, value)
                else:
                    best_value = min(best_value, value)
                    beta = min(beta, value)
                if beta <= alpha:
                    break
            return best_value

    def __square_list(self):
        return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

    def __generate_possible_step(self, current_state, current_player):
        # TODO
        valid_state = [[0 for row in range(constant.SIZE)] for column in range(constant.SIZE)]
        valid_step = []
        return valid_step

    def __evaluate_state(self, state):
        res = 0
        for square in self.__square_list():
            modifier = 1 if (state[square] == self.piece_color) else -1
            res += constant.BOARD_VALUE[square] * modifier
        return res

    def __change_state(self, step, state):
        state[step.row][step.column] = step.piece
        return state

    def __enemy_of(self, current_player):
        if current_player == constant.WHITE:
            return constant.BLACK
        else:
            return constant.WHITE
