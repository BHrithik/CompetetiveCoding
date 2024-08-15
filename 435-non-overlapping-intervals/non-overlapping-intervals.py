class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(0,len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                count+=1
                intervals[i+1][1] = min(intervals[i][1],intervals[i+1][1])
        return count