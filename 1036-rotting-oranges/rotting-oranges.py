class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()            
                for di,dj in directions:
                    nr,nc = r+di,c+dj
                    if nr < 0 or nr == len(grid) or nc <0 or nc == len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
            time += 1
        return -1 if fresh > 0 else time








        # oranges = []
        # time = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 2:
        #             oranges.append((i,j,time))
        # r_oranges = deque(oranges)
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # max_time = -1
        # while r_oranges:
        #     i,j,cur_time = r_oranges.popleft()
        #     max_time = max(cur_time,max_time)
        #     for di,dj in directions:
        #         if 0 <= i+di < len(grid) and 0<= j+dj <len(grid[0]) and grid[i+di][j+dj] == 1:
        #             grid[i+di][j+dj] = 2
        #             r_oranges.append((i+di,j+dj,cur_time+1))
        # flag= True
        # orange_present = False
        # for i in grid:
        #     for j in i:
        #         if j == 1:
        #             flag = False
        #             orange_present = True
        #         if j == 2:
        #             orange_present = True
        # if flag and orange_present:
        #     return max_time
        # elif not flag and orange_present:
        #     return -1
        # else:
        #     return 0










        # oranges = []
        # time = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 2:
        #             oranges.append((i,j,time))
        # r_oranges = deque(oranges)
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # max_time = -1
        # while r_oranges:
        #     i,j,cur_time = r_oranges.popleft()
        #     max_time = max(cur_time,max_time)
        #     for di,dj in directions:
        #         if 0 <= i+di < len(grid) and 0<= j+dj <len(grid[0]) and grid[i+di][j+dj] == 1:
        #             grid[i+di][j+dj] = 2
        #             r_oranges.append((i+di,j+dj,cur_time+1))
        # flag= True
        # orange_present = False
        # for i in grid:
        #     for j in i:
        #         if j == 1:
        #             flag = False
        #             orange_present = True
        #         if j == 2:
        #             orange_present = True
        # if flag and orange_present:
        #     return max_time
        # elif not flag and orange_present:
        #     return -1
        # else:
        #     return 0


