class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([n*n for n in nums])
        