class Solution:
    def rob(self, nums: List[int]) -> int:
#       [ 2, 7, 9, 3, 1]
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(rob1+i,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2