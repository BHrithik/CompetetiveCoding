class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        n = 0
        for i in sorted(counts.keys()):
            for j in range(counts[i]):
                nums[n] = i
                n = n+1
