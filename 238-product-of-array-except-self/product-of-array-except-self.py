class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum1 = 1
        pre_arr = [1]*len(nums)
        for i in range(0,len(nums)):
            sum1 *= nums[i]
            pre_arr[i] = sum1
        sum1 = 1
        post_arr = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            sum1 *= nums[i]
            post_arr[i] = sum1

        res = [1]*len(nums)
        for i in range(0,len(nums)):
            pr1 = pre_arr[i-1] if i-1 >= 0 else 1
            pr2 = post_arr[i+1] if i+1 < len(nums) else 1
            res[i] = pr1*pr2
        return res