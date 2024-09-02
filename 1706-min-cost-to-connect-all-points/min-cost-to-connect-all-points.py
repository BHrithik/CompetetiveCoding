class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adjList[i].append((dist,j))
        
        # Prim's ( Or as I like to call it Prem's)
        res = 0
        visited = set()
        mH = [[0,0]]
        heapq.heapify(mH)
        while len(visited) < n:
            cost, i = heapq.heappop(mH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiDist, nei in adjList[i]:
                if nei not in visited:
                    heapq.heappush(mH, (neiDist, nei))
        return res