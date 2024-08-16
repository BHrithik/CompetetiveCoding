class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(i,j):
            if i not in range(len(grid)) or j not in range(len(grid[0])):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j) # go down
            dfs(i-1,j) # go up
            dfs(i,j-1) # go left
            dfs(i,j+1) # go right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        return count



















        # ROWS = len(grid)
        # COLS = len(grid[0])
        # count = 0

        # def islandFound(m, n):
        #     if m < 0 or n < 0 or m >= ROWS or n >= COLS or grid[m][n] == "0":
        #         return
        #     grid[m][n] = "0"
        #     islandFound(m+1,n)
        #     islandFound(m,n+1)
        #     islandFound(m,n-1)
        #     islandFound(m-1,n)

        # for i in range(0,len(grid)):
        #     for j in range(0,len(grid[0])):
        #         if grid[i][j] == "1":
        #             islandFound(i,j)
        #             count = count + 1
        # return count
                