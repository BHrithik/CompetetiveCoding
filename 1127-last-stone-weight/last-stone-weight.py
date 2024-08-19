class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap)>1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap,-(abs(stone1)-abs(stone2)))
        return abs(maxHeap[0])