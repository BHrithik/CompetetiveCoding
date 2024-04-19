from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure A is the smaller array
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Partition A
            j = half - i - 2  # Partition B
            
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')
            
            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
