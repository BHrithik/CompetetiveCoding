class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = {}
        arr[0] = 0
        arr[1] = nums[0]
        for i in range(1,len(nums)):
            temp = nums[i]
            arr[i+1] = max(arr[i],arr[i-1]+temp)
        return arr[len(nums)]