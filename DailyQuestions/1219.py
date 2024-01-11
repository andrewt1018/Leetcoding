from typing import List 
    
def deepcopy(l):
    ret = []
    for row in l:
        ret.append(row.copy())
    return ret

class Solution:
    def __init__(self):
        self.visited = []
        self.currentScore = 0
        self.maxScore = -1
        self.rows = -1
        self.cols = -1

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.cols = len(grid[0])
        self.rows = len(grid)
        indices = []
        for i in range(self.rows):
            currRow = []
            for j in range(self.cols):
                if grid[i][j] == 0:
                    currRow.append(1)
                else:
                    currRow.append(0)
                    indices.append([i, j])
            self.visited.append(currRow)
        track = deepcopy(self.visited)

        # Find the first non-zero location
        start = False
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] != 0:
                    start = True
                    break
            if start:
                break
        if not start:
            return 0
        
        done = False
        for coord in indices:
            done = True
            self.findPath(grid, coord[0], coord[1], 0, deepcopy(track))   
        return self.maxScore
        
    def findPath(self, grid, i, j, score, visited):
        # print(f"Visiting ({i}, {j})")
        score = score + grid[i][j]
        # print(f"Score: {score}")
        visited[i][j] = 1

        # If there is a spot to the top
        if i != 0 and visited[i - 1][j] == 0:  
            self.maxScore = max(self.maxScore, self.findPath(grid, i - 1, j, score, deepcopy(visited)))

        # If there is a spot to the bottom
        if i != self.rows - 1 and visited[i + 1][j] == 0:  
            self.maxScore = max(self.maxScore, self.findPath(grid, i + 1, j, score, deepcopy(visited)))

        # If there is a spot to the left
        if j != 0 and visited[i][j - 1] == 0:
            self.maxScore = max(self.maxScore, self.findPath(grid, i, j - 1, score, deepcopy(visited)))
        
        # If there is a spot to the right
        if j != self.cols - 1 and visited[i][j + 1] == 0:
            self.maxScore = max(self.maxScore, self.findPath(grid, i, j + 1, score, deepcopy(visited)))
        
        self.maxScore = max(self.maxScore, score)
        return self.maxScore

grid = [[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]
grid1 = [[1, 1],
         [1, 1],
         [1, 1]]
grid2 = [[0,6,0],
         [5,8,7],
         [0,9,0]]
grid3 = [[1,0,7,0,0,0],
         [2,0,6,0,1,0],
         [3,5,6,7,4,2],
         [4,3,1,0,2,0],
         [3,0,5,0,20,0]]
sol = Solution()
maxGold = sol.getMaximumGold(grid3)
print(maxGold)