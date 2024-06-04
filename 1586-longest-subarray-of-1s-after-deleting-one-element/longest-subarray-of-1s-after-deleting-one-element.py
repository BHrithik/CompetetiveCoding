class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeroCount = 0
        Maxlen = 0
        for r in range(0,len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            while l<=r and zeroCount > 1:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            Maxlen = max(Maxlen,r-l)
        return Maxlen
                