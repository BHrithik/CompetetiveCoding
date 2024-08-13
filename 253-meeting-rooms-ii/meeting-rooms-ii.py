class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def getTime(intervals):
            if not intervals: return 0
            conflicts = []
            intervals.sort()
            for i in range(len(intervals)-1):
                end = intervals[i][1]
                start = intervals[i+1][0]
                if end > start:
                    conflicts.append(intervals[i+1])
                    intervals[i+1]=intervals[i]
            return 1 + getTime(conflicts)

        intervals.sort()
        return getTime(intervals)
        