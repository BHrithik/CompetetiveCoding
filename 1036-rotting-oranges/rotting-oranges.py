class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def countFreshAndRotten(grid): # Big O (n*m)
            count =0
            rotten = []
            for i in range(0,len(grid)):
                for j in range(0,len(grid[0])):
                    if grid[i][j] == 1:
                        count += 1
                    if grid[i][j] == 2:
                        rotten.append((i,j))
            return count, rotten
        def rot(rotten,fresh):  # Big always less than (o*m)
            new_rotten = []
            for i,j in rotten:
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        new_rotten.append((ni,nj))
                        fresh -= 1
            return new_rotten, fresh
        prevGrid = []
        time = 0
        fresh,rotten = countFreshAndRotten(grid)
        while rotten and fresh > 0:
            rotten,fresh = rot(rotten,fresh)
            time = time +1
        return time if fresh == 0 else -1