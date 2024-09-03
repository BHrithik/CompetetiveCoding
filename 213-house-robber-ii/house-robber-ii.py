class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robb(nums):
            cache = {}
            def dfs(i):
                if i >= len(nums):
                    return 0
                if i in cache:
                    return cache[i]
                cache[i] = nums[i] + max(dfs(i+2),dfs(i+3))
                return cache[i]
            return max(dfs(0),dfs(1))
        return max(robb(nums[:-1]),robb(nums[1:]))