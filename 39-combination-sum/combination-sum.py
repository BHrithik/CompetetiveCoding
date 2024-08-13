class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = []
        subSet = []
        def helper(i,cur_sum):
            if cur_sum == target:
                n.append(subSet.copy())
                return
            if cur_sum > target or i >= len(candidates):
                return
            subSet.append(candidates[i])
            helper(i, cur_sum+candidates[i])
            subSet.pop()
            helper(i+1, cur_sum)
        helper(0,0)
        return n