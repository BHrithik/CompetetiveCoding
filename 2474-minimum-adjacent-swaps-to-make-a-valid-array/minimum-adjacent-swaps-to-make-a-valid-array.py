class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        minNum = min(nums)
        maxNum = max(nums)
        nums2 = nums[::-1]
        posMin = nums.index(minNum)
        posMax = len(nums)-nums2.index(maxNum)-1
        if posMin > posMax:
            return posMin-1+len(nums)-posMax-1
        if posMin < posMax:
            return posMin+len(nums)-posMax-1
        if posMin==posMax:
            return 0