class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        self.res = 0
        def helper(idx,rem_sum):
            if idx == len(nums) and rem_sum == 0:
                return 1
            if idx == len(nums) and rem_sum != 0:
                return 0
            if (idx,rem_sum) in cache:
                return cache[idx,rem_sum]
            cache[idx,rem_sum] = helper(idx+1,rem_sum+nums[idx])+helper(idx+1,rem_sum-nums[idx])
            return cache[idx,rem_sum]
            # return helper(idx+1,rem_sum+nums[idx])+helper(idx+1,rem_sum-nums[idx])
        return helper(0,target)

