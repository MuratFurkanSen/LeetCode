class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        numMaps = dict()
        for i in range(1, 10):
            numMaps[i] = [[True for _ in range(9)] for __ in range(9)]
        self.board = board
        self.numMaps = numMaps
        self.updateMarks()
        while self.checkSingleOptions():
            self.updateMarks()

    def checkSingleOptions(self):
        changeDone = False
        for i in range(1, 10):
            currMap = self.numMaps[i]
            for j in range(9):
                currRow = self.getRow(currMap, j + 1)
                currCol = self.getCol(currMap, j + 1)
                currSqr = self.getSqr(currMap, j + 1)
                if currRow.count(True) == 1:
                    self.board[j][currRow.index(True)] = str(i)
                    changeDone = True
                if currCol.count(True) == 1:
                    self.board[currCol.index(True)][j] = str(i)
                    changeDone = True
                if currSqr.count(True) == 1:
                    extra = currSqr.index(True)
                    rowIndex = ((j // 3) * 3) + (extra // 3)
                    colIndex = ((j % 3) * 3) + (extra % 3)
                    self.board[rowIndex][colIndex] = str(i)
                    changeDone = True
        return changeDone

    def updateMarks(self):
        for i in range(1, 10):
            char = str(i)
            currMap = self.numMaps[i]
            for j in range(9):
                # Filling Rows In numMap
                if char in self.getRow(self.board, j + 1):
                    currMap[j] = [False for _ in range(9)]
                else:
                    for k in range(len(self.board)):
                        if self.board[j][k] != "." and currMap[j][k]:
                            currMap[j][k] = False
                # Filling Cols In numMap
                for row in range(len(self.board)):
                    currMap[row][j] = False if char in self.getCol(self.board, j + 1) else self.board[row][j] == "." and \
                                                                                           currMap[row][j]
                # Filling Square in numMap
                rowIndex = (j // 3) * 3
                colIndex = (j % 3) * 3
                for row in range(rowIndex, rowIndex + 3):
                    for col in range(colIndex, colIndex + 3):
                        currMap[row][col] = False if char in self.getSqr(self.board, j + 1) else self.board[row][
                                                                                                     col] == "." and \
                                                                                                 currMap[row][col]

    def getRow(self, board, rowID):
        return board[rowID - 1]

    def getCol(self, board, colID):
        col = list()
        for row in board:
            col.append(row[colID - 1])
        return col

    def getSqr(self, board, squareID):
        squareID -= 1
        rowIndex = (squareID // 3) * 3
        colIndex = (squareID % 3) * 3
        square = [i[colIndex:colIndex + 3] for i in board[rowIndex:rowIndex + 3]]
        square = [item for sublist in square for item in sublist]
        return square


s = Solution()
board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]
s.solveSudoku(board)
print(*board, sep="\n")
