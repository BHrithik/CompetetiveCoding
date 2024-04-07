class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        def robArr(houses):
            arr = {}
            arr[0] = 0
            arr[1] = houses[0]
            print(len(houses))
            for i in range(1,len(houses)):
                temp = houses[i]
                arr[i+1] = max(arr[i],arr[i-1]+temp)
            return arr[len(houses)]
        return max(robArr(nums[1:]),robArr(nums[:-1]))