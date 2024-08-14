class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for num2, num1 in zip(nums2,nums1):
            nums.append((num2,num1))
        nums.sort(reverse=True)
        minHeap = []
        cur_sum = 0
        res = 0
        for num2,num1 in nums:
            cur_sum += num1
            heapq.heappush(minHeap,num1)
            if len(minHeap) > k:
                cur_sum -= heapq.heappop(minHeap)
            if len(minHeap) == k:
                res = max(res,cur_sum*num2)
        return res