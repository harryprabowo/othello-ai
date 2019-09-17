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

    def isOnBoard(self, row, column):
        return row >= 0 and row <= 7 and column >= 0 and column <= 7

    def isValidMove(self, piece, row, col):
        if self.state[row][col] != constant.EMPTY or not isOnBoard(row, col):
            return False
        self.state[row][col] = piece
        other_piece = constant.BLACK if piece == constant.WHITE else constant.WHITE
        pieces_to_flip = []
        for row_direction, col_direction in constant.DIRECTION:
            row, column = row, col
            row += row_direction #first step in the direction
            column += col_direction #first step in the direction
            if isOnBoard(row, column) and self.state[row][column] == other_piece:
                row += row_direction
                column += col_direction
                if not isOnBoard(row, column):
                    continue
                while self.state[row][column] == other_piece:
                    row += row_direction
                    column += col_direction
                    if not isOnBoard(row, column): #break out of while loop, then continue in for loop
                        break
                if not isOnBoard(row, column):
                    continue
                if self.state[row][column] == piece:
                    #There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        row -= row_direction
                        column -= col_direction
                        if row == row and column == col:
                            break
                        pieces_to_flip.append([row, column])

        self[posx][posy] = ' ' #restore the empty space
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
