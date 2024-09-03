class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select
        # def quickSelect(l,r):
        #     pivot = nums[r]
        #     i = l
        #     for j in range(l,r):
        #         if nums[j] <= pivot:
        #             nums[i],nums[j] = nums[j],nums[i]
        #             i+=1
        #     nums[r], nums[i] = nums[i], nums[r]
        #     if len(nums)-i == k:
        #         return nums[i]
        #     elif len(nums)-i > k:
        #         return quickSelect(i+1,r)
        #     else:
        #         return quickSelect(l,i-1)
        # return quickSelect(0,len(nums)-1)

        minHeap = nums
        heapq.heapify(minHeap)
        k = len(nums)-k
        while k:
            heapq.heappop(minHeap)
            k -= 1
        return heapq.heappop(minHeap)