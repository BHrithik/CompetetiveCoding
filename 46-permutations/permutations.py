from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []
        visited = set()
        def dfs():
            if len(subSet) == len(nums):
                res.append(subSet.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    subSet.append(nums[i])
                    visited.add(nums[i])
                    dfs()
                    subSet.pop()
                    visited.remove(nums[i])
        dfs()
        return res