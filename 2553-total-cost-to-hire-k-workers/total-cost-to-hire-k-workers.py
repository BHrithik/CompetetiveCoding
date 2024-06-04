class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h = []
        n = len(costs)
        l = candidates
        r = n - candidates
        for i in range(l):
            heapq.heappush(h,(costs[i],i,1))
        for i in range(max(l,r),n):
            heapq.heappush(h,(costs[i],i,-1))
        total = 0
        r = r -1
        for _ in range(k):
            cost,index,direction = heapq.heappop(h)
            total = cost + total
            if l <= r:
                if direction == 1:
                    heapq.heappush(h,(costs[l],l,1))
                    l = l+1
                else:
                    heapq.heappush(h,(costs[r],r,-1))
                    r -= 1
        return total