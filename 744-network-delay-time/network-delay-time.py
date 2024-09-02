class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(n+1)}
        for a,b,t in times:
            adjList[a].append((t,b))
        # prims
        minH = [[0,k]]
        heapq.heapify(minH)
        visit = set()
        res = 0
        while minH:
            t, node = heapq.heappop(minH)
            if node in visit:
                continue
            res = max(res,t)
            visit.add(node)
            for time,nei in adjList[node]:
                if nei not in visit:
                    heapq.heappush(minH,(t+time,nei))
        if len(visit) < n:
            return -1
        return res
            