class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        cur = []
        def helper(i):
            if i >= len(nums):
                res.add(tuple(cur.copy()))
                return
            cur.append(nums[i])
            helper(i+1)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            cur.pop()
            helper(i+1)
        helper(0)
        return list(res)
            