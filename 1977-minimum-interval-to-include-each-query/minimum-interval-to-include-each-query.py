class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queryDict,minHeap,l = {},[],0
        for query in sorted(queries):
            while l<len(intervals) and intervals[l][0] <= query:
                heapq.heappush(minHeap,(intervals[l][1]-intervals[l][0]+1,intervals[l][1]))
                l+=1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            queryDict[query]=minHeap[0][0] if minHeap else -1
        return [queryDict[i] for i in queries]