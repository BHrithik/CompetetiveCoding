class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0
            if idx in cache:
                return cache[idx]
            if idx == len(nums)-1 or idx == len(nums)-2:
                return nums[idx]
            cache[idx] = nums[idx]+max(dfs(idx+2),dfs(idx+3))
            return cache[idx]
        return max(dfs(0),dfs(1))
