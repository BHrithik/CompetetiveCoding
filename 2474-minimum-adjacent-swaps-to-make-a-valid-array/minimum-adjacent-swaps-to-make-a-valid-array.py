class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        minNum = min(nums)
        maxNum = max(nums)
        nums2 = nums[::-1]
        posMin = nums.index(minNum)
        posMax = len(nums)-nums2.index(maxNum)-1
        print("min num",minNum)
        print("Position of min",posMin)
        print("max num",maxNum)
        print("Position of max",posMax)
        if posMin > posMax:
            #we can use a common move to use minimum moves
            movesForMin = posMin-1
            movesForMax = len(nums)-posMax-1
        if posMin < posMax:
            movesForMin = posMin
            movesForMax = len(nums)-posMax-1
        if posMin==posMax:
            return 0
        return movesForMin+movesForMax