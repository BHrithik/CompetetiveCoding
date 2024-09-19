class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToNum(time):
            nums = time.split(":")
            return int(nums[0])*60 + int(nums[1])
        
        nums = [timeToNum(time) for time in timePoints]
        nums.sort()
        minSum = (1440-nums[-1])+nums[0]
        for i in range(0,len(nums)-1):
            minSum = min(minSum, abs(nums[i-1]-nums[i]), abs(nums[i+1]-nums[i]))
        return minSum