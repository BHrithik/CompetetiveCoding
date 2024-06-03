class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count = 0
        flag = False
        while l < r:
            if nums[l]+nums[r] == k:
                print(f"{nums[l]} {nums[r]}")
                count = count+1
                flag = True
            if nums[l]+nums[r] < k:
                l = l+1
            if nums[l]+nums[r] > k:
                r = r-1
            if flag:
                l = l+1
                r = r-1
                flag = False
        return count