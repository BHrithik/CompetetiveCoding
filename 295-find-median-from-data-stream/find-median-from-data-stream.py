class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num) # initially add the number to maxHeap
        heapq.heappush(self.minHeap,-(heapq.heappop(self.maxHeap))) # remove the largest number from maxheap and add it to min heap
        if len(self.minHeap) != len(self.maxHeap)+1: # if length difference is more than 1 remove element from min heap and add it to maxHeap
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap)>len(self.maxHeap): # since min heap will always have more elements we can return the top of the heap as median
            return self.minHeap[0]
        else: # since the count is even we need to get the top of 2 heaps and divide them with 2 to return min and max
            return (self.minHeap[0]-self.maxHeap[0])/2
        