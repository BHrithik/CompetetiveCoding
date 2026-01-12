class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # if mid is greater than right, min is to the right of mid
            if nums[m] > nums[r]:
                l = m + 1
            else:
                # min is at mid or to the left of mid
                r = m
        return nums[l]