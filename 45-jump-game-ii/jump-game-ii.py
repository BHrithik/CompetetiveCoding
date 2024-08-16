from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l, r = 0, 0
        res = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,nums[i]+i)
            l = r+1
            r = farthest
            res += 1
        return res