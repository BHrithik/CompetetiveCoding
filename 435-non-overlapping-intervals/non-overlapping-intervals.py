class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for start,end in intervals[1:]:
            if prevEnd > start:
                count += 1
                prevEnd = min(prevEnd,end)
            else:
                prevEnd = end
                # prevEnd = min(prevEnd,end)
        return count
