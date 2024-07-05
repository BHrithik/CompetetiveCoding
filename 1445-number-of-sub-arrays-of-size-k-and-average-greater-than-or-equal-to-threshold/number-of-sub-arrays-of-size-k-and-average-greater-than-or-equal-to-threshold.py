class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        thresholdSum = k * threshold
        cur_sum = sum(arr[:k])
        for i in range(k,len(arr)):
            if cur_sum >= thresholdSum:
                c += 1
            cur_sum = cur_sum - arr[i-k]+arr[i]
        if cur_sum >= thresholdSum:
                c += 1
        return c