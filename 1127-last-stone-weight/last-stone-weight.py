class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-i for i in stones]
        heapq.heapify(minHeap)
        print(minHeap)
        while len(minHeap)>1:
            stone1 = heapq.heappop(minHeap)
            stone2 = heapq.heappop(minHeap)
            heapq.heappush(minHeap,-(abs(stone1)-abs(stone2)))
        return abs(minHeap[0])