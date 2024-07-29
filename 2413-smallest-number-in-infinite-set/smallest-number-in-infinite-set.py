class SmallestInfiniteSet:

    def __init__(self):
        self.infinite_count = 1
        self.heap = []
        self.set = set()
    
    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap)
            self.set.remove(res)
            return res
        else:
            res = self.infinite_count
            self.infinite_count += 1
            return res

    def addBack(self, num: int) -> None:
        if num < self.infinite_count and num not in self.set:
            heapq.heappush(self.heap,num)
            self.set.add(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)