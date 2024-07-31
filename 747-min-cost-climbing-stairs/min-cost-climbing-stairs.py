class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(n):
            if n >= len(cost):
                return 0            
            if n in cache:
                return cache[n]
            cache[n] =  min(dfs(n+1)+cost[n],dfs(n+2)+cost[n])
            return cache[n]
        return min(dfs(0),dfs(1))