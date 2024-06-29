class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        for i in nums1:
            if i not in nums2:
                ans1.add(i)
        for i in nums2:
            if i not in nums1:
                ans2.add(i)
        return [list(ans1),list(ans2)]