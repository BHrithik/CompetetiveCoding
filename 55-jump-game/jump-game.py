class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxReach = 0
        for i in range(0,len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach,i+nums[i])
            if maxReach >= len(nums)-1:
                return True
        return False