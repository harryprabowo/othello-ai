import constant
from step import Step


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

    def is_on_board(self, row, column):
        return row >= 0 and row <= 7 and column >= 0 and column <= 7

    def is_empty(self, row, column):
        return self.state[row][column]

    def isValidMove(self, piece, row, column):
        if (not (self.is_empty(row,column) or self.is_on_board(row, column))):
            return False
        self.state[row][column] = piece
        other_piece = constant.BLACK if piece == constant.WHITE else constant.WHITE
        pieces_to_flip = []
        for row_direction, column_direction in constant.DIRECTION:
            step = Step(row, column)
            step.row += row_direction #first step in the direction
            step.column += column_direction #first step in the direction
            if self.is_on_board(step.row, step.column) and self.state[step.row][step.column] == other_piece:
                step.row += row_direction
                step.column += column_direction
                if not self.is_on_board(step.row, step.column):
                    continue
                while self.state[step.row][step.column] == other_piece:
                    step.row += row_direction
                    step.column += column_direction
                    if not self.is_on_board(step.row, step.column): #break out of while loop, then continue in for loop
                        break
                if not self.is_on_board(step.row, step.column):
                    continue
                if self.state[step.row][step.column] == piece:
                    #There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        step.row -= row_direction
                        step.rowcolumn -= column_direction
                        if row == row and column == column:
                            break
                        pieces_to_flip.append([step.row, step.column])

        self.state[row][column] = constant.EMPTY #restore the empty space
        if len(pieces_to_flip) == 0: #If no tiles were flipped, this is not a valid move.
            return False
        return pieces_to_flip

    def getValidMoves(self, piece):
        #langkah valid
        validMoves = []
        for row in range(8):
            for column in range(8):
                if self.isValidMove(piece, row, column) != False:
                    validMoves.append([row, column])
        return validMoves

    def getBoardCopy(self):
        #copy board
        copyBoard = Board()
        copyBoard.state = self.state
        return copyBoard

    def getBoardWithValidMoves(self, piece):
        #nunjukin langkah valid
        copyBoard = self.getBoardCopy()
        for row, column in getValidMoves(copyBoard, self):
            copyBoard[row][column] = '.'
        return copyBoard
