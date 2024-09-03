class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = n-1
            while l < r:
                if nums[l] + nums[r] == target:
                    if i != l and i != r:
                        res.add(tuple([nums[i],nums[l],nums[r]]))
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return list(res)

















        # res = set()
        # nums.sort()
        # for i in range(0,len(nums)):
        #     target = -nums[i]
        #     l = i+1
        #     r = len(nums)-1
        #     while l < r:
        #         cur_sum = nums[l]+nums[r]
        #         if cur_sum == target:
        #             res.add(tuple([nums[i],nums[l],nums[r]]))
        #             l += 1
        #             r -= 1
        #         elif cur_sum < target:
        #             l += 1
        #         else:
        #             r -= 1
        # return list(res)