class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            if not (0<=i<len(grid) and 0<=j<len(grid[0])) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res