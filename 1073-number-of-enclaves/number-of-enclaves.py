class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0 
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        # First, clear all land cells connected to the borders
        for i in range(m):
            dfs(i, 0)  # Left column
            dfs(i, n-1)  # Right column
        for j in range(n):
            dfs(0, j)  # Top row
            dfs(m-1, j)  # Bottom row
        
        # Then, count the enclaves
        return sum([sum(i) for i in grid])
