class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in set_nums: # Potential start of a sequence
                length = 1
                while n+length in set_nums:
                    length += 1
                longest = max(length,longest)
        return longest