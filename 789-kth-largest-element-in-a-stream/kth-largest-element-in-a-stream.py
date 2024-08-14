class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.n = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.n:
            heapq.heappop(self.heap)
        res = heapq.heappop(self.heap)
        heapq.heappush(self.heap,res)
        return res