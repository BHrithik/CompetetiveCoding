class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            p1 = nums[i]
            p2 = target - nums[i]
            if p2 in nums:
                j = nums.index(p2)
                if i != j:
                    return [i,j]
                
