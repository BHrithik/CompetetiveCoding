class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        for i in range(0,len(nums)):
            ans.append(product)
            product = product * nums[i]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*product
            product= nums[i] * product
        print(ans)
        return ans