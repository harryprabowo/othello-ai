import constant
import step


class Board:
    # Private
    def __init__(self):
        self.__initialize_state()

    def __initialize_state(self):
        self.state = [[ constant.EMPTY for row in range(constant.SIZE)] for column in range(constant.SIZE)]
        self.__initialize_start_piece()

    def __initialize_start_piece(self):
        self.state[3][3] = constant.WHITE
        self.state[4][4] = constant.WHITE
        self.state[4][3] = constant.BLACK
        self.state[3][4] = constant.BLACK

    # Public
    def get_state(self):
        return self.state

    def change_state(self, step):
        self.state[step.row][step.column] = step.piece
