class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return nums[0]
        def rob2(nums:List[int]) -> int:
            memo = {}
            def helper(i):
                if i >= len(nums):
                    return 0
                if i in memo:
                    return memo[i]
                rob_current = nums[i]+helper(i+2)
                skip_current = helper(i+1)
                memo[i] = max(rob_current, skip_current)
                return memo[i]
            return helper(0)
        return max(rob2(nums[1:]),rob2(nums[:-1]))