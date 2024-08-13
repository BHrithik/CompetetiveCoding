class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subSet = []
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subSet.copy()))
                return
            # new_index = i
            # if nums[i] in 
            subSet.append(nums[i])
            dfs(i+1)
            subSet.pop()
            dfs(i+1)
        dfs(0)
        return res