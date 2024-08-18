class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        dp = {0}
        for i in range(0,len(nums)):
            new_dp = set()
            for t in dp:
                if t+nums[i] == target:
                    return True
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp = new_dp
        return False










        # if sum(nums)%2:return False
        # target = sum(nums)//2
        # possible_sums = {0}
        # for i in nums:
        #     next_sums = set()
        #     for sums in possible_sums:
        #         next_sums.add(i+sums)
        #         if i+sums == target:
        #             return True
        #     possible_sums.update(next_sums)
        # return False

