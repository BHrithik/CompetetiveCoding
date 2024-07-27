class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        no_sides = len(nums)
        nums.sort()
        cur_sum = sum(nums)
        for i in range(len(nums),2,-1):
            if cur_sum-nums[i-1] > nums[i-1]:
                if i == 2:
                    return -1
                return cur_sum
            cur_sum -= nums[i-1]
        return -1
            