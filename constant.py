SIZE = 8
DEFAULT_DEPTH = 6

# pieces
EMPTY = 0
BLACK = 1
WHITE = 2
BORDER = 3

def enemy_of(player):
    if player == WHITE:
        return BLACK
    else:
        return WHITE

# directions
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

# positional heuristic
BOARD_VALUE = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 100, -20, 10, 5, 5, 10, -20, 100, 0,
    0, -20, -50, -2, -2, -2, -2, -50, -20, 0,
    0, 10, -2, -1, -1, -1, -1, -2, 10, 0,
    0, 5, -2, -1, -1, -1, -1, -2, 5, 0,
    0, 5, -2, -1, -1, -1, -1, -2, 5, 0,
    0, 10, -2, -1, -1, -1, -1, -2, 10, 0,
    0, -20, -50, -2, -2, -2, -2, -50, -20, 0,
    0, 100, -20, 10, 5, 5, 10, -20, 100, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# bound
MAX_VALUE = sum(map(abs, BOARD_VALUE))
MIN_VALUE = -MAX_VALUE
