class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        total = sum(nums)
        res = float('inf')
        cur_sum = sum(nums[:total])
        l = 0
        for i in range(total,len(nums)):
            cur_sum -= nums[l]
            l += 1
            cur_sum += nums[i]
            res = min(res,total-cur_sum)
        cur_sum = sum(nums[-total:])
        for i in range(total):
            cur_sum += nums[i]
            cur_sum -= nums[-total+i]
            res = min(res,total-cur_sum)
        return res
        