class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        cur_set = []
        def helper(i):
            if i >= len(nums):
                sets.append(cur_set.copy())
                return
            #Decision to add the current element
            cur_set.append(nums[i])
            helper(i+1)
            cur_set.pop()
            helper(i+1)
        helper(0)
        return sets
            