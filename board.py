import constant
import step

class Board:
    # Private
    def __init__(self):
        self.__initializeState()

    def __initializeState(self):
        self.state = [[ constant.EMPTY for row in range(constant.SIZE)] for column in range(constant.SIZE)]
        self.__initializeStartPiece()

    def __initializeStartPiece(self):
        self.state[3][3] = constant.WHITE
        self.state[4][4] = constant.WHITE
        self.state[4][3] = constant.BLACK
        self.state[3][4] = constant.BLACK

    # Public
    def getState(self):
        return self.state

    def changeState(self, step):
        self.state[step.row][step.column] = step.piece
