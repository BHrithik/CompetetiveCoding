class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        memo = {}
        def helper(i, arr):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            rob_current = arr[i]+helper(i+2, arr)
            skip_current = helper(i+1, arr)
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        skip_first_house = helper(0,nums[1:])
        memo = {}
        skip_last_house = helper(0, nums[:-1])
        return max(skip_first_house, skip_last_house)