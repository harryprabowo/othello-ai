import constant
class Board:
    def __init__(self):
        initializeState()

    def initializeState(self, size):
        self.state = [[ constant.EMPTY for row in range(constant.SIZE)] for column in range(constant.SIZE)]
        initializeStartPiece()
    
    def initializeStartPiece(self):
        self.state[3][3] = constant.WHITE
        self.state[4][4] = constant.WHITE
        self.state[4][3] = constant.BLACK
        self.state[3][4] = constant.BLACK
