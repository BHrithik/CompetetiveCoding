class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1
        for i in nums:
            if i == 0:
                cur_max = 1
                cur_min = 1
                continue
            temp = cur_max*i
            cur_max = max(i,cur_max*i,cur_min*i)
            cur_min = min(i,cur_min*i, temp)
            res = max(res, cur_max)
        return res