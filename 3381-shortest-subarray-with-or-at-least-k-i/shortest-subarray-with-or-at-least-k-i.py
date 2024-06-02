class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) > k:
            return 1
        m = 0
        cnt = float('inf')
        possible = False
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i,len(nums)):
                temp = temp | nums[j]
                if temp >= k:
                    possible = True
                    cnt = min(cnt,j-i+1)
        return cnt if possible else -1