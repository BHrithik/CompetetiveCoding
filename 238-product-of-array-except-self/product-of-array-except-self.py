class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = 1
        postfixProduct = 1
        res = [0]* n
        for i in range(n):
            res[i] = prefixProduct
            prefixProduct *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= postfixProduct
            postfixProduct *= nums[i]
        return res