class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        def dfs(i, a):
            if a == target:
                res.append((combination.copy()))
                return
            if i > len(candidates)-1 or a > target: return
            combination.append(candidates[i])
            dfs(i+1,a+candidates[i])
            combination.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,a)
        dfs(0,0)
        return list(res)















        # candidates.sort()
        # res = []
        # subSet = []
        # def bcktrk(i,cur_sum):
        #     if cur_sum == target:
        #         res.append(subSet.copy())
        #         return
        #     if cur_sum > target or i>= len(candidates):
        #         return
        #     subSet.append(candidates[i])
        #     bcktrk(i+1,cur_sum+candidates[i])
        #     subSet.pop()
        #     while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
        #         i = i+1
        #     bcktrk(i+1, cur_sum)
        # bcktrk(0,0)
        # return list(res)