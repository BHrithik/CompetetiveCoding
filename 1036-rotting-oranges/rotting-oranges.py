class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def AllRotten(grid):
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    if grid[i][j] == 1:
                        return False
            return True
        def rot(grid):
            newGrid = deepcopy(grid)
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    if grid[i][j] == 2:
                        # print(f"found rotten at {i} {j}")
                        if i-1 >=0 and grid[i-1][j] == 1:
                            newGrid[i-1][j] = 2
                        if j-1 >=0 and grid[i][j-1] == 1:
                            newGrid[i][j-1] = 2
                        if j+1 <len(grid[0]) and grid[i][j+1] == 1:
                            newGrid[i][j+1] = 2
                        if i+1 <len(grid) and grid[i+1][j] == 1:
                            newGrid[i+1][j] = 2
            return newGrid
        prevGrid = []
        time = 0
        flag = AllRotten(grid)
        while grid != prevGrid and not flag:
            prevGrid = deepcopy(grid)
            grid = rot(grid)
            time = time +1
            flag = AllRotten(grid)
        if flag:
            return time
        else:
            return -1