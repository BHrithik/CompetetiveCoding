class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def helper(nums):
            rob1, rob2 = 0, 0
            for i in range(0,len(nums)):
                temp = rob2
                rob2 = max(rob1+nums[i],rob2)
                rob1 = temp
            return rob2
            # cache = {}
            # def rob(i):
            #     if i > len(nums)-1:
            #         return 0
            #     if i in cache:
            #         return cache[i]
            #     cache[i] = nums[i]+max(rob(i+2),rob(i+3))
            #     return cache[i]
            # return max(rob(0),rob(1))
        return max(helper(nums[1:]),helper(nums[:-1]))









        # if len(nums) <= 3:
        #     return max(nums)
        # def robb(nums):
        #     rob1, rob2 = 0, 0
        #     for num in nums:
        #         temp = max(rob1+num,rob2)
        #         rob1 = rob2
        #         rob2 = temp
        #     return rob2
        # return max(robb(nums[:-1]),robb(nums[1:]))