class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possibilites = []
        for row in range(9):
            possible = []
            for col in range(9):
                if board[row][col] == '.':
                    possible.append([])
                    continue
                possible.append(self.checkPossibleValues(row, col, board, ))

    
    def find3x3(self, row, col, board):
        """
        Find the numbers in the quadrant containing the coordinate
        """

        # Find the origin of the quadrant that the coordinate belongs to
        dr, dc = tuple(map(lambda x : x % 3,[row, col]))
        ox, oy = tuple((map(lambda x, y: x - y, [row, col], [dr, dc])))

        # Loop through the 3x3 uadrant 
        ret = []
        for r in range(ox, ox + 3):
            for c in range(oy, oy + 3):
                elem = board[r][c]
                if elem != '.':
                    ret.append(elem)
        return ret

    def transposeBoard(self, board):
        """
        Transposes the current board and returns a new boardT
        """


    def checkPossibleValues(self, row, col, board, boardT):
        """
        Checks the possible values that can be placed at a specific coordinate 
        by performing the horizontal, vertical, and quadrant checks
        """
        ret = []
        quadrant = self.find3x3(row, col, board)
        for i in range(1, 10, 1): # Check each value from 1 - 9
            i = str(i)
            if (i in board[row]) or (i in boardT[col]) or (i in quadrant):
                continue
            ret.append(i)
        return ret
        

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
boardT = []
for r in range(9):
    row = []
    for c in range(9):
        row.append(board[c][r])
    boardT.append(row)
# for r in range(9):
#     for c in range(9):
#         boardT[r][c] = board[c][r]
for i in board:
    print(i)
print()
for i in boardT:
    print(i)
print()

# sol = Solution()
# print(sol.checkPossibleValues(0, 3, board, boardT))


