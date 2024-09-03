from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # max_reach = 0
        # cur_end = 0
        # count = 0
        # for i in range(len(nums)):
        #     max_reach = max(max_reach,nums[i]+i)
        #     if i == cur_end:
        #         count += 1 # we need to jump
        #         cur_end = max_reach
        #         if cur_end >= len(nums)-1:
        #             break
        # return count
        if len(nums) == 1:
            return 0
        cur_end = 0
        maxReach = 0
        count = 0
        for i in range(0,len(nums)):
            maxReach = max(maxReach, i+nums[i])
            if i == cur_end:
                count += 1
                cur_end = maxReach
                if maxReach >= len(nums)-1:
                    return count