import constant
class Board:
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