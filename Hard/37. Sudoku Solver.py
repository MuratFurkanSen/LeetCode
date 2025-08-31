class Solution:
    board = None
    cells = None

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.setup()
        self.solve()

    def setup(self) -> None:
        cell_candidates = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '.':
                    candidates = self.get_candidates(i, j)
                    cell_candidates.append([i, j, 0, candidates])
        self.cells = cell_candidates

    def validate(self, row_index: int, col_index: int, num: int) -> bool:
        # Check Rows
        str_num = str(num)
        if str_num in self.board[row_index]:
            return False

        # Check Columns
        for i in range(9):
            if str_num == self.board[i][col_index]:
                return False

        # Check Squares
        box = []
        for k in range(3 * (row_index // 3), 3 * (row_index // 3 + 1)):
            for t in range(3 * (col_index // 3), 3 * (col_index // 3 + 1)):
                if str_num == self.board[k][t]:
                    return False

        # Not Found
        return True

    def solve(self) -> None:
        # Go with Solid Ones First
        placed = True
        while placed:
            placed_cells = []
            placed = False
            for cell in self.cells:
                if len(cell[3]) == 1:
                    row, col, index, candidates = cell
                    self.place(row, col, candidates[0])
                    placed_cells.append(cell)
                    placed = True
            for cell in placed_cells:
                self.cells.remove(cell)

        # Solid Methods got Stuck
        cell_index = 0
        counter = 0
        while cell_index < len(self.cells):
            row, col, candidate_index, candidates = self.cells[cell_index]
            while candidate_index < len(candidates):
                counter += 1
                if self.validate(row, col, candidates[candidate_index]):
                    self.cells[cell_index][2] = candidate_index
                    row, col, candidate_index, candidates = self.cells[cell_index]
                    self.board[row][col] = str(candidates[candidate_index])
                    cell_index += 1
                    break
                else:
                    candidate_index += 1
            else:
                self.cells[cell_index][2] = 0
                row, col, candidate_index, candidates = self.cells[cell_index]
                self.board[row][col] = '.'
                cell_index -= 1
                self.cells[cell_index][2] += 1
        print(counter)

    def get_candidates(self, i: int, j: int) -> list[int]:
        candidates = list(range(1, 10))
        # Look for Row
        for k in range(9):
            if self.board[i][k] != '.' and int(self.board[i][k]) in candidates:
                candidates.remove(int(self.board[i][k]))
        # Look for Column
        for k in range(9):
            if self.board[k][j] != '.' and int(self.board[k][j]) in candidates:
                candidates.remove(int(self.board[k][j]))
        # Look for Square
        for k in range(3 * (i // 3), 3 * (i // 3 + 1)):
            for t in range(3 * (j // 3), 3 * (j // 3 + 1)):
                if self.board[k][t] != '.' and int(self.board[k][t]) in candidates:
                    candidates.remove(int(self.board[k][t]))

        return candidates

    def remove_candidate(self, row: int, col: int) -> None:
        for i in range(len(self.cells)):
            cell = self.cells[i]
            cell_row, cell_col, cell_index, cell_values = cell
            if cell_row == row and cell_col == col:
                self.cells.remove(cell)
                return

    def place(self, row: int, col: int, num: int) -> None:
        for i in range(len(self.cells)):
            cell = self.cells[i]
            cell_row, cell_col, cell_index, cell_values = cell
            if cell_row == row and cell_col == col:
                continue
            elif cell_row == row and num in cell[3]:
                cell[3].remove(num)
            elif cell_col == col and num in cell[3]:
                cell[3].remove(num)
            elif (cell_row in list(range((row // 3) * 3, (row // 3 + 1) * 3))) and (
                    cell_col in list(range((col // 3) * 3, (col // 3 + 1) * 3))) and num in cell[3]:
                cell[3].remove(num)
        self.board[row][col] = str(num)


if __name__ == '__main__':
    s = Solution()
    board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "9", ".", ".", "1", ".", ".", "3", "."],
             [".", ".", "6", ".", "2", ".", "7", ".", "."],
             [".", ".", ".", "3", ".", "4", ".", ".", "."],
             ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "2", "5", ".", "6", "4", ".", "."],
             [".", "8", ".", ".", ".", ".", ".", "1", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    s.solveSudoku(board)
    print(*board, sep="\n")
