class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToNum(time):
            nums = time.split(":")
            return int(nums[0])*60 + int(nums[1])
        
        # nums = [timeToNum(time) for time in timePoints]
        timePoints.sort(key=lambda x: timeToNum(x))
        minSum = (1440-timeToNum(timePoints[-1]))+timeToNum(timePoints[0])
        for i in range(0,len(timePoints)-1):
            minSum = min(minSum, abs(timeToNum(timePoints[i-1])-timeToNum(timePoints[i])), abs(timeToNum(timePoints[i+1])-timeToNum(timePoints[i])))
        return minSum