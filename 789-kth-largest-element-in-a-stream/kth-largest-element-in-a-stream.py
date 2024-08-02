class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.largest = k
        heapq.heapify(self.arr)
        while len(self.arr) > k:
            heapq.heappop(self.arr)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        while len(self.arr) > self.largest:
            heapq.heappop(self.arr)
        return self.arr[0]