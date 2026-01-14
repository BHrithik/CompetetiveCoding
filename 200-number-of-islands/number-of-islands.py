class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i,j):
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == "0":
                return
            grid[i][j] = "0" # marking as visited so that we don't come here again
            helper(i+1,j) # exploring right
            helper(i-1,j) # exploring left
            helper(i,j+1) # exploring up
            helper(i,j-1) # exploring down
            return
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1 # We found land
                    helper(i,j) # let us explore how big this island is mark them as visited
        return count