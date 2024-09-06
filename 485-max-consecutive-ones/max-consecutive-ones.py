class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        n = 0
        for num in nums:
            if num == 0:
                n = 0
            else:
                n += 1
            res = max(res, n)
        return res