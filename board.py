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

    def isOnBoard(step.row, step.column):
        #mengecek apakah pada Arena atau gak
        return step.row >= 0 and step.row <= 7 and step.column >= 0 and step.column <= 7

    def isValidMove(self, tile, posx, posy):
        #mengecek apakah langkah valid
        kosong = ' '
        if self[posx][posy] != kosong or not isOnBoard(posx, posy):
            return False
        self[posx][posy] = tile
        if tile == constant.WHITE:
            otherTile = constant.BLACK
        else:
            otherTile = constant.WHITE
        tilesToFlip = []
        for xdirect, ydirect in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            #[0, 1] berarti ke bawah
            #[1, 1] berarti ke kiri bawah
            #[1, 0] berarti ke kiri
            #[1, -1] berarti ke kiri atas
            #[0, -1] berarti ke atas
            #[-1, -1] berarti ke kanan atas
            #[-1, 0] berarti ke kanan
            #[-1, 1] berarti ke kanan bawah
            step.row, step.column = posx, posy
            step.row += xdirect #first step in the direction
            step.column += ydirect #first step in the direction
            if isOnBoard(step.row, step.column) and self[step.row][step.coumn] == otherTile:
                step.row += xdirect
                step.column += ydirect
                if not isOnBoard(step.row, step.column):
                    continue
                while self[step.row][step.column] == otherTile:
                    step.row += xdirect
                    step.column += ydirect
                    if not isOnBoard(step.row, step.column): #break out of while loop, then continue in for loop
                        break
                if not isOnBoard(step.row, step.column):
                    continue
                if self[step.row][step.column] == tile:
                    #There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        step.row -= xdirect
                        step.column -= ydirect
                        if step.row == posx and step.column == posy:
                            break
                        tilesToFlip.append([step.row, step.column])

        self[posx][posy] = ' ' #restore the empty space
        if len(tilesToFlip) == 0: #If no tiles were flipped, this is not a valid move.
            return False
        return tilesToFlip

    def getValidMoves(self, tile):
        #langkah valid
        validMoves = []
        for step.row in range(8):
            for step.column in range(8):
                if isValidMove(self, tile, step.row, step.column) != False:
                    validMoves.append([step.row, step.column])
        return validMoves

    def getBoardCopy(self):
        #copy board
        copyBoard = __init__(self)
        for step.row in range(8):
            for step.column in range(8):
                copyBoard[step.row][step.column] = self[step.row][step.column]
        return copyBoard

    def getBoardWithValidMoves(self, tile):
        #nunjukin langkah valid
        copyBoard = getBoardCopy(self)
        for step.row, step.column in getValidMoves(copyBoard, self):
            copyBoard[step.row][step.column] = '.'
        return copyBoard
