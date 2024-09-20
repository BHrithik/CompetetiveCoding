class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        nums1 = [int(i) for i in nums1]
        nums2 = [int(i) for i in nums2]
        for i in range(len(nums1)-1,-1,-1):
            if nums1[i] != 0:
                break
        nums1 = nums1[:i+1]
        for i in range(len(nums2)-1,-1,-1):
            if nums2[i] != 0:
                break
        nums2 = nums2[:i+1]
        c = 0
        while c < min(len(nums1),len(nums2)):
            if nums1[c] == nums2[c]:
                c += 1
                continue
            elif nums1[c] < nums2[c]:
                return -1
            else:
                return 1
        if len(nums1) == len(nums2):
            return 0
        if c >= len(nums1):
            return -1
        else:
            return 1