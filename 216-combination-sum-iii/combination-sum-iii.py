class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1,10)
        res = []
        subSet = []
        def dfs(i):
            if len(subSet) == k and sum(subSet) == n:
                res.append(subSet.copy())
                return
            if sum(subSet) > n or i >= len(nums) or len(subSet) > k:
                return
            subSet.append(nums[i])
            dfs(i+1)
            subSet.pop()
            dfs(i+1)
        dfs(0)
        return res

            
