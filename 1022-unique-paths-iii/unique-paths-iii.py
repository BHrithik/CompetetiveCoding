class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        non_obstacle_cells = 0
        start = end = None
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:  # Count non-obstacle cells
                    non_obstacle_cells += 1
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
        
        def dfs(x, y, visited_count):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == -1 or visited[x][y]:
                return 0
            if (x, y) == end:
                return visited_count == non_obstacle_cells
            
            visited[x][y] = True
            paths = (dfs(x+1, y, visited_count+1) +
                     dfs(x-1, y, visited_count+1) +
                     dfs(x, y+1, visited_count+1) +
                     dfs(x, y-1, visited_count+1))
            visited[x][y] = False  # backtrack
            return paths
        
        visited = [[False] * n for _ in range(m)]
        return dfs(start[0], start[1], 1)  # Start counting from the start cell

