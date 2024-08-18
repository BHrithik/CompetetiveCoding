class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        visited = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i in visited:
                return visited[i]
            cur = 1
            for n in range(i,len(nums)):
                if nums[i] < nums[n]:
                    cur = max(cur,1+dfs(n))
            visited[i] = cur
            return visited[i]
        for i in range(0,len(nums)):
            res = max(res,dfs(i))
        return res












        # dp = [1]*len(nums)
        # for i in range(len(nums)-2,-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i],1+dp[j])
        # return max(dp)