class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_l = len(nums1)+len(nums2)
        median = total_l//2
        cur_count = 0
        res = -1
        l1=0
        l2=0
        lasteles = []
        while cur_count != median+1:
            if l1 < len(nums1) and (l2 >= len(nums2) or nums1[l1] < nums2[l2]):
                lasteles.append(nums1[l1])
                l1+=1
            else:
                lasteles.append(nums2[l2])
                l2+=1
            cur_count += 1
        return lasteles[-1] if total_l%2 == 1 else (lasteles[-1]+lasteles[-2])/2