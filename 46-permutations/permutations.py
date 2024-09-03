from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms

















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