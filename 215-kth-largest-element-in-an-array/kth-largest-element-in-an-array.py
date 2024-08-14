class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]
        minHeap = nums
        heapq.heapify(minHeap)
        k = len(nums)-k
        while k:
            heapq.heappop(minHeap)
            k -= 1
        return heapq.heappop(minHeap)