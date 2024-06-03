class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count = 0
        while l < r:
            cur_total = nums[l]+nums[r]
            if cur_total == k:
                count = count+1
                l = l+1
                r = r-1
            if cur_total < k:
                l = l+1
            if cur_total > k:
                r = r-1
        return count