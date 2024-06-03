class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        counter = 0
        arr = []
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                nums[counter] = nums[i]
                counter += 1
        print(nums)
        print(zeroes)
        print(counter)
        for i in range(0,zeroes):
            nums[counter+i] = 0
