class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subSet = []
        def dfs(i):
            if i == len(nums):
                res.append(subSet[::])
                return
            subSet.append(nums[i])
            dfs(i+1)
            subSet.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i = i+1
            dfs(i+1)
        dfs(0)
        return res