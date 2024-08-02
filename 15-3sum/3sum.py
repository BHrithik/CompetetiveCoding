class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0,len(nums)):
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                cur_sum = nums[l]+nums[r]
                if cur_sum == target and l!=i and r!=i:
                    res.add(tuple(sorted([nums[l],nums[i],nums[r]])))
                    l += 1
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    r -= 1
        return list(res)