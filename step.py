class Step:
    def __init__(self, row, column, piece):
        self.row = row
        self.column = column
        self.piece = piece

    def getStateValue(self):
        return self.row * 10 + self.column;
