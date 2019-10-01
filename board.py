from constant import *
import step


class Board:
    # Private
    def __init__(self):
        self.__initialize_state()

    def main_board(self):
        return [square for square in range(11, 89) if 1 <= (square % 10) <= 8]

    def __initialize_state(self):
        self.state = [BORDER] * 100
        for square in self.main_board():
            self.state[square] = EMPTY

        self.__initialize_start_piece()

    def __initialize_start_piece(self):
        self.state[44] = WHITE
        self.state[45] = BLACK
        self.state[54] = BLACK
        self.state[55] = WHITE

    # Public
    def get_state(self):
        return self.state

    def get_square(self, row, column):
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

    def make_move(self, move, player):
        self.state[move] = player
        for direction in DIRECTIONS:
            self.make_flips(move, player, direction)
        return self.state

    def make_flips(self, move, player, direction):
        bracket = self.find_bracket(move, player, direction)
        if not bracket:
            return
        square = move + direction
        while square != bracket:
            self.state[square] = player
            square += direction

    def has_bracket(self, move, player):
        for direction in DIRECTIONS:
            if not self.find_bracket(move, player, direction):
                return True
        return False

    def is_legal(self, move, player):
        return self.state[move] == EMPTY and self.has_bracket(move, player)

    def possible_moves(self, player):
        return [square for square in self.main_board() if self.is_legal(square, player)]

    def any_possible_move(self, player):
        return any(self.is_legal(square, player) for square in self.main_board())
