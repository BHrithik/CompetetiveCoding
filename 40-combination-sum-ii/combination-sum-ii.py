class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subSet = []
        def bcktrk(i,cur_sum):
            if cur_sum == target:
                res.append(subSet.copy())
                return
            if cur_sum > target or i>= len(candidates):
                return
            subSet.append(candidates[i])
            bcktrk(i+1,cur_sum+candidates[i])
            subSet.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i = i+1
            bcktrk(i+1, cur_sum)
        bcktrk(0,0)
        return list(res)