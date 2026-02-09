class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        i = 1
        res = 0
        while i < n-1:
            if arr[i-1] < arr[i] > arr[i+1]:
                # peak found
                left = i-1
                while left > 0 and arr[left-1] < arr[left]:
                    left -=1
                
                right = i+1
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1
                
                res = max(res, right-left+1)
                # we expanded from peak so no need of scanning elements again from the left so we can skip to right
                i = right
            else:
                i += 1
        return res
            