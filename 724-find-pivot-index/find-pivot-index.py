class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for idx,ele in enumerate(nums):
            rightSum = rightSum - ele
            if rightSum == leftSum:
                return idx
            leftSum += ele
        return -1