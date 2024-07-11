class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix_arr = [0]*n
        postfix_arr = [0]*n
        prefix = 1
        for i in range(0,n):
            prefix *= nums[i]
            prefix_arr[i] = prefix
        print(prefix_arr)
        postfix = 1
        for i in reversed(range(0,n)):
            postfix *= nums[i]
            postfix_arr[i] = postfix
        print(postfix_arr)
        res = [0]*n
        for i in range(0,n):
            if i-1 < 0:
                prod1 = 1
            else:
                prod1 = prefix_arr[i-1]
            if i+1 >= n:
                prod2 = 1
            else:
                prod2 = postfix_arr[i+1]
            res[i] = prod1*prod2
        print(res)
        return res
