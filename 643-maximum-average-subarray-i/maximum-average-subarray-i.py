class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        max_sum = sum(nums[:k])
        cur = max_sum
        for new in range(len(nums)-k):
            cur = cur - nums[new] + nums[new+k]
            if cur > max_sum: max_sum = cur
        return max_sum/k