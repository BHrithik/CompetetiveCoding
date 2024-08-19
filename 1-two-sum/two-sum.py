class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            if target-nums[i] in numDict:
                return [i,numDict[target-nums[i]]]
            numDict[nums[i]] = i
        # new_nums = [(value,index) for index,value in enumerate(nums)]
        # new_nums.sort()
        # l = 0
        # r = len(nums)-1
        # while l < r:
        #     if new_nums[l][0]+new_nums[r][0] == target:
        #         return [new_nums[l][1],new_nums[r][1]]
        #     elif new_nums[l][0]+new_nums[r][0] > target:
        #         r -= 1
        #     else:
        #         l += 1
        
                
