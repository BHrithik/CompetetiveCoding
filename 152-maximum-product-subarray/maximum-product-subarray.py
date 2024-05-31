class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax = 1, 1
        res = max(nums)
        for i in nums:
            if i == 0:
                curMin,curMax = 1, 1
            temp = i*curMin
            curMin = min(i*curMin,i*curMax,i)
            curMax = max(i*curMax,temp,i)
            res = max(res,curMax)      
        return res  
