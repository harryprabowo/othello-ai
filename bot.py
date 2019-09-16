import constant


class Bot:
    def __init__(self, pieceColor, depth=2):
        self.pieceColor = pieceColor
        self.depth = depth

    def move(self, currentState):
        return self.dfs(currentState, self.pieceColor, self.depth, -constant.INFVAL, constant.INFVAL)

    def dfs(self, currentState, currentPlayer, remainingDepth, alpha, beta):
        if (remainingDepth == 0):
            return self.evaluateState(currentState)
        else:
            # TODO
            possibleStep = self.generatePossibleStep(currentState, currentPlayer)
            for step in possibleStep:
                nextState = self.changeState(step, currentState)
                value = self.dfs(nextState, self.enemyOf(currentPlayer), remainingDepth - 1, alpha, beta)
                if (currentPlayer == self.pieceColor):
                    alpha = max(alpha, value)
                else:
                    beta = min(beta, value)
                if beta >= alpha:
                    break
            return 1

    def generatePossibleStep(self, currentState, currentPlayer):
        # TODO
        validState = [[0 for row in range(constant.SIZE)] for column in range(constant.SIZE)]
        validStep = []
        return validStep

    def evaluateState(self, state):
        # TODO
        return 1

    def changeState(self, step, state):
        # TODO
        return state

    def enemyOf(self, currentPlayer):
        if (currentPlayer == constant.WHITE):
            return constant.BLACK
        else:
            return constant.WHITE
