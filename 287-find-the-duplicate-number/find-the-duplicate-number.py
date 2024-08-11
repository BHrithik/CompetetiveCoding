class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = {}
        for i in nums:
            if i not in hashSet:
                hashSet[i] = 1
            else:
                return i