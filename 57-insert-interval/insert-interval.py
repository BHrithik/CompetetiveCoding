class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        inserted = False
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start >= newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break
            elif end >= newInterval[0]:
                intervals.insert(i + 1, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)
        print(intervals)
        l = 1
        res = [intervals[0]]
        while l < len(intervals):
            if intervals[l][0] <= res[-1][1]: # We need to meerge here
                # res[-1][0] = min(res[-1][0],intervals[l][0])
                res[-1][1] = max(res[-1][1],intervals[l][1])
            else:
                res.append(intervals[l])
            l+=1
        return res
            
