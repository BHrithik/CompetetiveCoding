class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                # No overlap, just append the interval
                merged_intervals.append(interval)
            else:
                # Overlapping, merge the intervals
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        return merged_intervals
