class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums = sorted([i for i in set(nums)])
        l, r, maxLen = 0, 0, 0
        while r < len(nums)-1:
            if nums[r]+1 == nums[r+1]:
                maxLen = max(maxLen,r+1-l)
            else:
                l = r+1
            r += 1 
        return maxLen+1

# [0,3,7,2,5,8,4,6,0,1]
# [0,1,2,3,4,5,6,7,8]
# [100,4,200,1,3,2]
# [1,2,3,4,100,200,1,3,2]