class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = [int(i) for i in version1.split('.')]
        nums2 = [int(i) for i in version2.split('.')]
        
        # Compare the two versions number by number
        for i in range(max(len(nums1), len(nums2))):
            v1 = nums1[i] if i < len(nums1) else 0
            v2 = nums2[i] if i < len(nums2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
