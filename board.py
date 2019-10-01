from constant import *
import step


class Board:
    # Private
    def __init__(self):
        self.__initialize_state()

    def __main_board(self):
        return [square for square in range(11, 89) if 1 <= (square % 10) <= 8]

    def __initialize_state(self):
        self.state = [BORDER] * 100
        for square in self.__main_board():
            self.state[square] = EMPTY

        self.__initialize_start_piece()

    def __initialize_start_piece(self):
        self.state[44] = WHITE
        self.state[45] = BLACK
        self.state[54] = BLACK
        self.state[55] = WHITE

    # Public
    def get_state(self, row, column):
        position = "{}{}".format(row, column)
        position = int(position)
        return self.state[position]

    def get_opponent(self, player):
        return BLACK if player is WHITE else WHITE

    def find_bracket(self, square, player, direction):
        bracket = square + direction
        if self.state[bracket] == player:
            return None
        opponent = self.get_opponent(player)
        while self.state[bracket] == opponent:
            bracket += direction
        return None if self.state[bracket] in (BORDER, EMPTY) else bracket
