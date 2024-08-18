class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1

        for i in nums:
            if i == 0:
                cur_min, cur_max = 1, 1
                continue
            temp = cur_max
            cur_max = max(i*cur_max,i*cur_min,i)
            cur_min = min(i*temp,i*cur_min,i)
            res = max(cur_max,res)
        return res