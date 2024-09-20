class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (2**31)-1
        gates = deque([])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    gates.append((i,j))
        while gates:
            for i in range(len(gates)):
                i,j = gates.popleft()
                for di,dj in directions:
                    if 0 <= i+di < len(rooms) and 0 <= j+dj < len(rooms[i+di]) and rooms[i+di][j+dj] == INF:
                        rooms[i+di][j+dj] = rooms[i][j]+1
                        gates.append((i+di,j+dj))
        print(rooms)
        return rooms