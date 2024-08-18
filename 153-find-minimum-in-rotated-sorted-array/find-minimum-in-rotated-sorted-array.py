class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        while l <= r:
            # If the array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1  # Move to the unsorted right part
            else:
                r = m - 1  # Move to the unsorted left part
        
        return res