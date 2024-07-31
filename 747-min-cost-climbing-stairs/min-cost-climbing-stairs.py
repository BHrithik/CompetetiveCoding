class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-4,-1,-1):
            cost[i] = cost[i] + min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
        
        # cache = {}
        # def dfs(n):
        #     if n >= len(cost):
        #         return 0            
        #     if n in cache:
        #         return cache[n]
        #     cache[n] =  min(dfs(n+1)+cost[n],dfs(n+2)+cost[n])
        #     return cache[n]
        # dfs(0)
        # return min(cache[0],cache[1])