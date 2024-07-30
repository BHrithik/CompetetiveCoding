class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mergedIntervals = []
        for interval in intervals:
            if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1],interval[1])
        return mergedIntervals