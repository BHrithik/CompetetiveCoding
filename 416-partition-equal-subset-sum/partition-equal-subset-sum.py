class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:return False
        target = sum(nums)//2
        possible_sums = {0}
        for i in nums:
            next_sums = set()
            for sums in possible_sums:
                next_sums.add(i+sums)
                if i+sums == target:
                    return True
            possible_sums.update(next_sums)
        return False

