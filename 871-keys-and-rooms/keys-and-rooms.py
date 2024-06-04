class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        def bfs(num):
            if num in keys:
                return
            if num not in keys:
                keys.add(num)
            for i in rooms[num]:
                bfs(i)
        bfs(0)

        return len(keys) == len(rooms)