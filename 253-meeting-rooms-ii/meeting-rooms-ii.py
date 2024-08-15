class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def getTime(intervals):
            if not intervals: return 0
            conflicts = []
            for i in range(len(intervals)-1):
                if intervals[i][1] > intervals[i+1][0]:
                    conflicts.append(intervals[i+1])
                    intervals[i+1]=intervals[i]
            return 1 + getTime(conflicts)

        intervals.sort()
        return getTime(intervals)
        