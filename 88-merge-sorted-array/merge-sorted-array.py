class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,len(nums2)):
            nums1[len(nums1)-len(nums2)+i] = nums2[i]
        print(nums1)
        nums1.sort()
        # n1 = 0
        # n2 = 0
        # while n1 < len(nums1)-len(nums2) and n2 < len(nums2):
        #     if nums1[n1] <= nums2[n2]:
        #         n1 += 1
        #     else:
        #         temp = nums1[n1]
        #         nums1[n1] = nums2[n2]
        #         n2 += 1
                
        