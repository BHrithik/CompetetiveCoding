class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queryDict = {}
        new_queries = queries[:]
        queries.sort()
        minHeap = []
        res = []
        l=0
        for query in queries:
            while l<len(intervals) and intervals[l][0] <= query:
                heapq.heappush(minHeap,(intervals[l][1]-intervals[l][0]+1,intervals[l][1]))
                l+=1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            if minHeap:
                queryDict[query]=minHeap[0][0]
            else:
                queryDict[query]= -1
        return [queryDict[i] for i in new_queries]