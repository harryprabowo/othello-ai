import constant
class Board:
    def __init__(self):
        initializeState()

    def initializeState(self, size):
        #TODO : make state representation
        self.state = [[ 0 for row in range(constant.SIZE)] for column in range(constant.SIZE)]
