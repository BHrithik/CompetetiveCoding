class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for n in nums:
            counts[n] += 1
        n = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[n] = i
                n = n+1
