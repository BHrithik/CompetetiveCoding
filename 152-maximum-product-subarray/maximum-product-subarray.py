class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax = 1, 1
        res = max(nums)
        for i in nums:
            if i == 0:
                curMin,curMax = 1, 1
            temp = i*curMax
            curMax = max(i*curMax,i*curMin,i)
            curMin = min(i*curMin,temp,i)
            res = max(res,curMax)      
        return res  
