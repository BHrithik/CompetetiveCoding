class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def helper(i,j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for di, dj in directions:
                helper(i+di,j+dj)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    helper(i,j)
                    res += 1
        return res