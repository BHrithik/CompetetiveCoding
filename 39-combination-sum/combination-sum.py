class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        cur_arr = []
        def helper(i, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.add(tuple(cur_arr.copy()))
            #Deciding to take the current i we are on
            cur_arr.append(candidates[i])
            helper(i, total+candidates[i])
            #Deciding not to take the current i we are on
            cur_arr.pop()
            helper(i+1, total)
        helper(0,0)
        return list(res)