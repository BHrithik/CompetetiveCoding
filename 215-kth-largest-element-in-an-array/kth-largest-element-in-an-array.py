
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        while k:
            num = -1 * heapq.heappop(nums)
            k -= 1
        return num
        