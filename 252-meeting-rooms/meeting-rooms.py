class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(0,len(intervals)-1):
            start,end = intervals[i]
            if end > intervals[i+1][0]:
                return False
        return True