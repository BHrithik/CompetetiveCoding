class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        ans = 0
        minNum = min(nums)
        maxNum = max(nums)
        posMin = nums.index(minNum)
        nums = nums[::-1]
        posMax = len(nums)-nums.index(maxNum)-1
        if posMin > posMax:
            return posMin-1+len(nums)-posMax-1
        if posMin < posMax:
            return posMin+len(nums)-posMax-1
        if posMin==posMax:
            return 0