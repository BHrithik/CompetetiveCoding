class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = []
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    oranges.append((i,j,time))
        r_oranges = deque(oranges)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_time = -1
        while r_oranges:
            i,j,cur_time = r_oranges.popleft()
            max_time = max(cur_time,max_time)
            for di,dj in directions:
                if 0 <= i+di < len(grid) and 0<= j+dj <len(grid[0]) and grid[i+di][j+dj] == 1:
                    grid[i+di][j+dj] = 2
                    r_oranges.append((i+di,j+dj,cur_time+1))
        flag= True
        orange_present = False
        for i in grid:
            for j in i:
                if j == 1:
                    flag = False
                    orange_present = True
                if j == 2:
                    orange_present = True
        if flag and orange_present:
            return max_time
        elif not flag and orange_present:
            return -1
        else:
            return 0


