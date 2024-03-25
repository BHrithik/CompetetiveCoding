class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def islandFound(m, n):
            if m < 0 or n < 0 or m >= ROWS or n >= COLS or grid[m][n] == "0":
                return
            grid[m][n] = "0"
            islandFound(m+1,n)
            islandFound(m,n+1)
            islandFound(m,n-1)
            islandFound(m-1,n)

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    islandFound(i,j)
                    count = count + 1
        return count
                