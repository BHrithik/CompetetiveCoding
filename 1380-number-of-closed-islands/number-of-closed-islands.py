class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = {}
        count = 0
        currentIsland = []
        def dfs(i,j):
            nonlocal count
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i,j) in currentIsland:
                return True
            if grid[i][j] == 1:
                return True
            currentIsland.append((i,j))
            islands[(i,j)]= dfs(i+1,j) and dfs(i-1,j) and dfs(i,j+1) and dfs(i,j-1)
            return islands[(i,j)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in islands and dfs(i, j):
                    count += 1
                currentIsland = []
        return count