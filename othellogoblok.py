import sys
import random

def initBoard():
    #Init Papan Arena
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board

def drawBoard(board):
    #ngeprint Papan Arena
    border = '+-+-+-+-+-+-+-+-+'
    print(border)
    for y in range(8):
        for x in range(8):
            print('|%s' % (board[x][y]), end='')
        print('|')
        print(border)

def resetBoard(board):
    #Reset Papan Arena
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

def isOnBoard(x,y):
    #mengecek apakah pada Arena atau gak
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

def isValidMove(board, tile, posx, posy):
    #mengecek apakah langkah valid
    kosong = ' '
    if board[posx][posy] != kosong or not isOnBoard(posx, posy):
        return False
    board[posx][posy] = tile
    if tile == 'W':
        otherTile = 'B'
    else:
        otherTile = 'W'
    tilesToFlip = []
    for xdirect, ydirect in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = posx, posy
        x += xdirect #first step in the direction
        y += ydirect #first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirect
            y += ydirect
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirect
                y += ydirect
                if not isOnBoard(x, y): #break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                #There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirect
                    y -= ydirect
                    if x == posx and y == posy:
                        break
                    tilesToFlip.append([x, y])
        
    board[posx][posy] = ' ' #restore the empty space
    if len(tilesToFlip) == 0: #If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip

def getValidMoves(board, tile):
    #langkah valid
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getBoardCopy(board):
    #copy board
    copyBoard = initBoard()
    for x in range(8):
        for y in range(8):
            copyBoard[x][y] = board[x][y]
    return copyBoard

def getBoardWithValidMoves(board, tile):
    #nunjukin langkah valid
    copyBoard = getBoardCopy(board)
    for x, y in getValidMoves(copyBoard, tile):
        copyBoard[x][y] = '.'
    return copyBoard

def getScore(board):
    #skor
    whitescore = 0
    blackscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'W':
                whitescore += 1
            if board[x][y] == 'B':
                blackscore += 1
    return {'W':whitescore, 'B':blackscore}

def enterPlayerTile():
    #milih warna player
    tile = ''
    while not (tile == 'W' or tile == 'B'):
        print('Pilih warna pemain :')
        print('type W or B')
        tile = input().upper()
    if tile == 'W':
        return ['W', 'B']
    else:
        return ['B', 'W']

def firstTurn():
    #randomizer first turn
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def retry():
    #main lagi
    print('Mau mencoba lagi?')
    print('type yes or no')
    return input().lower().startswith('y')

def makeMove(board, tile, posx, posy):
    tilesToFlip = isValidMove(board, tile, posx, posy)
    if tilesToFlip == False:
        return False
    board[posx][posy] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def isCorner(x, y):
    #apakah mojok
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    #gerak pemain
    numinput = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Masukkan langkahmu...')
        print('type kolom dan baris tanpa spasi untuk langkah, contoh 31')
        print('type quit untuk keluar dari game')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if len(move) == 2 and move[0] in numinput and move[1] in numinput:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Input tidak valid!')
    return [x, y]

def getComputerMove(board, computerTile):
    #gerak komputer
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if isCorner(x, y):
            return [x, y]
    bestScore = -1
    for x, y in possibleMoves:
        copyBoard = getBoardCopy(board)
        makeMove(copyBoard, computerTile, x, y)
        score = getScore(copyBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def showPoints(playerTile, computerTile):
    #tampilin skor
    scores = getScore(mainBoard)
    print('Skor Player   : %s.' % (scores[playerTile]))
    print('Skor Komputer : %s.' % (scores[computerTile]))

#Main
print('OTHELLO GOBLOK')
while True:
    mainBoard = initBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = True
    turn = firstTurn()
    print(turn + ' jalan duluan.')

    while True:
        if turn == 'player':
            # Player's turn.
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Anda keluar dari permainan.')
                sys.exit()            
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
            
            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'

        else:
            # Computer's turn.
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Sekarang giliran komputer. Tekan Enter. ')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)
            if getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'player'

    # END
    drawBoard(mainBoard)
    scores = getScore(mainBoard)
    print('Skor kubu putih : %s.' % (scores['W']))
    print('Skor kubu hitam : %s.' % (scores['B']))
    if scores[playerTile] > scores[computerTile]:
        print('Selamat Anda menang!')
    elif scores[playerTile] < scores[computerTile]:
        print('Yaaah, Anda kalah.')
    else:
        print('Kalian seri!')
    if not retry():
        break