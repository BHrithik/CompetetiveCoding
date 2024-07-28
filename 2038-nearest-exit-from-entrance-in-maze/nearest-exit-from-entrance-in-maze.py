class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        shortest_path = float('inf')
        count = 0
        queue = deque([(entrance[0],entrance[1],count)])
        while queue:
            i,j, cur_count = queue.popleft()
            if (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1) and [i,j] != entrance:
                return cur_count
            for di,dj in directions:
                ni = di+i
                nj = dj+j
                if 0 <= ni <= len(maze)-1 and 0 <= nj <= len(maze[0])-1 and maze[ni][nj]=="." and (ni,nj) not in visited:
                    queue.append((ni,nj,cur_count+1))
                    visited.add((ni,nj))
        return -1
                
                

        # def dfs(i, j, count):
        #     nonlocal shortest_path
        #     if (i, j) in visited:
        #         return
        #     visited.add((i, j))
        #     if (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1):
        #         if [i, j] != entrance:
        #             shortest_path = min(shortest_path, count)
        #             return
        #     for di, dj in directions:
        #         ni, nj = i + di, j + dj
        #         if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] == '.' and (ni, nj) not in visited:
        #             dfs(ni, nj, count + 1)
        #     visited.remove((i, j))
        
        dfs(entrance[0], entrance[1], 0)
        return shortest_path if shortest_path != float('inf') else -1
