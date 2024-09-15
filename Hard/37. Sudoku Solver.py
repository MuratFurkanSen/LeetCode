class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        numMaps = dict()
        for i in range(1, 10):
            char = str(i)
            numMaps[i] = [[True for _ in range(9)] for __ in range(9)]

            # Check Row
            for rowIndex in range(len(board)):
                if char in board[rowIndex]:
                    numMaps[i][rowIndex] = [False for _ in range(9)]
            # Check Col
            for colIndex in range(len(board[0])):
                col = list()
                for j in range(len(board)):
                    col.append(board[j][i])
            if char in col



s = Solution()
board = [["1", "2", "3"]]
s.solveSudoku(board)
