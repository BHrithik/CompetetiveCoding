class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left2right = []
        cur_pro = 1
        for i in nums:
            cur_pro *= i
            left2right.append(cur_pro)
        right2left = []
        cur_pro = 1
        for i in range(len(nums)-1,-1,-1):
            cur_pro *= nums[i]
            right2left.append(cur_pro)
        right2left = right2left[::-1]
        res = []
        print(left2right)
        print(right2left)
        for i in range(len(nums)):
            p1 = left2right[i-1] if i > 0 else 1
            p2 = right2left[i+1] if i < len(right2left)-1 else 1
            res.append(p1*p2)
        return res