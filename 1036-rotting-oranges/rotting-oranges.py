class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # def AllRotten(grid):
        #     for i in range(0,len(grid)):
        #         for j in range(0,len(grid[0])):
        #             if grid[i][j] == 1:
        #                 return False
        #     return True
        def countFreshAndRotten(grid):
            count =0
            rotten = []
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    if grid[i][j] == 1:
                        count += 1
                    if grid[i][j] == 2:
                        rotten.append((i,j))
            return count, rotten
        def rot(rotten,fresh):
            new_rotten = []
            for i,j in rotten:
                if i-1 >=0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    new_rotten.append((i-1,j))
                    fresh -= 1
                if j-1 >=0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_rotten.append((i,j-1))
                    fresh -= 1
                if j+1 <len(grid[0]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_rotten.append((i,j+1))
                    fresh -= 1
                if i+1 <len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    new_rotten.append((i+1,j))
                    fresh -= 1
            return new_rotten, fresh
        prevGrid = []
        time = 0
        fresh,rotten = countFreshAndRotten(grid)
        while rotten and fresh > 0:
            rotten,fresh = rot(rotten,fresh)
            time = time +1
        if fresh == 0:
            return time
        else:
            return -1