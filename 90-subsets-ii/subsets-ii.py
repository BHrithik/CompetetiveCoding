class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subSet = []
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(sorted(subSet.copy())))
                return
            subSet.append(nums[i])
            dfs(i+1)
            subSet.pop()
            dfs(i+1)
        dfs(0)
        return res
            