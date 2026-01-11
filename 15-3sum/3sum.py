class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0,len(nums)):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                cur_sum = nums[left]+nums[right]
                if cur_sum == target and (nums[i],nums[left],nums[right]) not in res:
                    res.add((nums[i],nums[left],nums[right]))
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return list(res)