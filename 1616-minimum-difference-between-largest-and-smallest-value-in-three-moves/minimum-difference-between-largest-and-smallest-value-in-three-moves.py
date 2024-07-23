class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        min_nums = sorted(heapq.nsmallest(4,nums))
        max_nums = sorted(heapq.nlargest(4,nums))
        res = float("inf")
        for i in range(4):
            res = min(res, max_nums[i]-min_nums[i])
        return res