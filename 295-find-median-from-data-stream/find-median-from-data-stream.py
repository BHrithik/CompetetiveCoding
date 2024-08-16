class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        heapq.heappush(self.minHeap,-(heapq.heappop(self.maxHeap)))
        if len(self.minHeap) > len(self.maxHeap)+1:
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0]-self.maxHeap[0])/2
        