class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = Counter(nums)
        return not all([True if numDict[i] == 1 else False for i in numDict])