class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indexes = []
        for i in range(0,len(nums)):
            if nums[i] == x:
                indexes.append(i)
        ans = []
        print(indexes)
        for i in queries:
            if i > len(indexes):
                ans.append(-1)
            else:
                ans.append(indexes[i-1])
        return ans