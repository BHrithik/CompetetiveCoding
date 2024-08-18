class Solution:
    def rob(self, nums: List[int]) -> int:
#       [ 2, 7, 9, 3, 1]
#         i       
        cache = {}     
        def dfs(i):
            if i > len(nums)-1:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = nums[i] + max(dfs(i+2),dfs(i+3))
            return cache[i]
        return max(dfs(0),dfs(1))
        








        # rob1, rob2 = 0, 0
        # for i in nums:
        #     temp = max(rob1+i,rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2