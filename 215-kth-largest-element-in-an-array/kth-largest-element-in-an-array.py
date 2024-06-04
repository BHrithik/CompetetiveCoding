class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush(h,-i)
        element = 0
        for _ in range(k):
            element = heapq.heappop(h)
        return -element