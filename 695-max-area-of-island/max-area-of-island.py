class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def helper(i,j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1 + helper(i+1,j) + helper(i-1,j) + helper(i,j+1) + helper(i,j-1)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = helper(i,j)
                    res = max(area,res)
        return res