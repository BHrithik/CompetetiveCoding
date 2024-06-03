class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        max_sum = 0
        l, r = 0, 0
        zero_count = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_count += 1
                while l <= r and  zero_count > k:
                    if nums[l] == 0:
                        zero_count -= 1
                    cur_sum -= 1
                    l = l+1
            cur_sum = cur_sum + 1
            max_sum = cur_sum if cur_sum > max_sum else max_sum
            r = r+1
        return max_sum



        
        return r-l