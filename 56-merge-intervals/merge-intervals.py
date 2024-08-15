class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        l = 1
        while l < len(intervals):
            if intervals[l][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1],intervals[l][1])
            else:
                res.append(intervals[l])
            l += 1
        return res
