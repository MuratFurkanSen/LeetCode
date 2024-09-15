class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Row Check
        for row in board:
            if not self.checkIntCopy(row):
                return False

        # Col Check
        for i in range(len(board[0])):
            col = list()
            for j in range(len(board)):
                col.append(board[j][i])
            if not self.checkIntCopy(col):
                return False

        # Square Check
        for rowIndex in range(0, len(board), 3):
            for colIndex in range(0, len(board), 3):
                square = [i[colIndex:colIndex + 3] for i in board[rowIndex:rowIndex + 3]]
                square = [item for sublist in square for item in sublist]
                if not self.checkIntCopy(square):
                    return False
        return True

    def checkIntCopy(self, nums: list[str]) -> bool:
        numsCheck = list()
        for num in nums:
            if num == ".":
                continue
            if num not in numsCheck:
                numsCheck.append(num)
            else:
                return False
        return True


board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

sol = Solution()
print(sol.isValidSudoku(board))
