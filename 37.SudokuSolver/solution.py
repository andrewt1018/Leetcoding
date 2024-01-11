class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        solSpace = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append([])
            solSpace.append(row)

        boardT = self.transposeBoard(board)
        possible_values = []    # Store all of the possible values in every block
        done = False
        while not done:
            self.print_board(board)
            done = True
            added = False   # Bool to check if an element has been added
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        continue
                    # If the board is not completed yet
                    done = False

                    # Fill in based on possible values at a coordinate
                    possible_values = self.checkPossibleValues(row, col, board, boardT)
                    solSpace[row][col] = possible_values
                    if len(possible_values) == 1:
                        print(f"Adding {possible_values[0]} at ({row}, {col})")
                        # Add the possible value to the board if there's only one possible value
                        board[row][col] = possible_values[0]
                        boardT[col][row] = possible_values[0]
                        solSpace[row][col] = []
                        added = True
                        continue

                   
            if not added:
                 # Fill in based on unique values of a coordinate in its quadrant
                for row in range(9):
                    for col in range(9):
                        unique_possibilities = self.findUniqueQuadrantPossibilities(row, col, solSpace)
                        if len(unique_possibilities) == 1:
                            print(f"Rol: {row}, Col: {col}")
                            print("Unique Quad: ", unique_possibilities)
                            # print("Solution space: ")
                            # self.print_solSpace(solSpace)
                            board[row][col] = unique_possibilities[0]
                            boardT[col][row] = unique_possibilities[0]
                            solSpace[row][col] = []
                            added = True
                            continue
            

                        unique_possibilities = self.findUniqueColPossibilities(row, col, solSpace)
                        if len(unique_possibilities) == 1:
                                print(f"Rol: {row}, Col: {col}")
                                print("Unique Col: ", unique_possibilities)
                                # print("Solution space: ")
                                # self.print_solSpace(solSpace)
                                board[row][col] = unique_possibilities[0]
                                boardT[col][row] = unique_possibilities[0]
                                solSpace[row][col] = []
                                added = True
                                continue
                    
                        unique_possibilities = self.findUniqueRowPossibilities(row, col, solSpace)
                        if len(unique_possibilities) == 1:
                                print(f"Rol: {row}, Col: {col}")
                                print("Unique Row: ", unique_possibilities)
                                # print("Solution space: ")
                                # self.print_solSpace(solSpace)
                                board[row][col] = unique_possibilities[0]
                                boardT[col][row] = unique_possibilities[0]
                                solSpace[row][col] = []
                                added = True
                                continue

            if not added:
                return solSpace

    def findUniqueQuadrantPossibilities(self, row, col, solSpace):
        """
        Find the unique solutions given a coordinate with its 3x3 grid
        """

        # Find the origin of the quadrant that the coordinate belongs to
        dr, dc = tuple(map(lambda x : x % 3,[row, col]))
        ox, oy = tuple((map(lambda x, y: x - y, [row, col], [dr, dc])))
        l = []
        for i in range(3):
            for j in range(3):
                if i == (row - ox) and j == (col - oy):
                    continue
                for x in solSpace[ox + i][oy + j]:
                    l.append(int(x))
        l = list(set(l))
        ret = []
        for num in solSpace[row][col]:
            if int(num) not in l:
                ret.append(num)
        return ret

    def findUniqueRowPossibilities(self, row, col, solSpace):
        """
        Find the unique solutions of given a coordinate in the row it resides
        """

        l = []
        for i in range(9):
            if i == col:
                continue
            for num in solSpace[row][i]:
                l.append(num)
        l = list(set(l))
        ret = []
        for num in solSpace[row][col]:
            if num not in l:
                ret.append(num)
        return ret

    def findUniqueColPossibilities(self, row, col, solSpace):
        """
        Find the unique solutions of given a coordinate in the column it resides
        """

        l = []
        for i in range(9):
            if i == row:
                continue
            for num in solSpace[i][col]:
                l.append(num)
        l = list(set(l))
        ret = []
        for num in solSpace[row][col]:
            if num not in l:
                ret.append(num)
        return ret

    def find3x3(self, row, col, board):
        """
        Find the numbers in the quadrant containing the coordinate
        """

        # Find the origin of the quadrant that the coordinate belongs to
        dr, dc = tuple(map(lambda x : x % 3,[row, col]))
        ox, oy = tuple((map(lambda x, y: x - y, [row, col], [dr, dc])))

        # Loop through the 3x3 quadrant 
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
        boardT = []
        for r in range(9):
            row = []
            for c in range(9):
                row.append(board[c][r])
            boardT.append(row)
        return boardT

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

    def print_board(self, board):
        for row in board:
            for elem in row:
                print(elem, end=" ")
            print()
        print()
    
    def print_solSpace(self, solSpace):
        for row in solSpace:
            for col in row:
                print(col, end=" ")
            print()
    
        

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

board2 = [[".",".","9","7","4","8",".",".","."],
          ["7",".",".",".",".",".",".",".","."],
          [".","2",".","1",".","9",".",".","."],
          [".",".","7",".",".",".","2","4","."],
          [".","6","4",".","1",".","5","9","."],
          [".","9","8",".",".",".","3",".","."],
          [".",".",".","8",".","3",".","2","."],
          [".",".",".",".",".",".",".",".","6"],
          [".",".",".","2","7","5","9",".","."]]
x = board2
for i in x:
    print(i)
print()

sol = Solution()
solSpace = sol.solveSudoku(x)
for row in solSpace:
    for col in row:
        print(col, end=" ")
    print()

# for i in range(9):
#     for j in range(9):
#         if board[i][j] != ".":
#             continue
#         print(f"i={i}, j={j}")
#         print(sol.checkPossibleValues(i, j, board, boardT))
#         print()



