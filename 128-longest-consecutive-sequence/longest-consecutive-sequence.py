class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num-1 not in num_set: # pt start of a sequence
                start = num
                end = num+1
                while end in num_set:
                    end += 1
                res = max(end-start,res)
        return res