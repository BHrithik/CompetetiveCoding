class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        MAX = (2**31) - 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            for di, dj in directions:
                nr,nc = r+di, c+dj
                if nr not in range(len(rooms)) or nc not in range(len(rooms[0])) or rooms[nr][nc] != MAX:
                    continue
                rooms[nr][nc] = rooms[r][c]+1
                q.append((nr,nc))