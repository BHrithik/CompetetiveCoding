class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            #left sorted array
            if nums[l] <= nums[m]:
                if target > nums[m] or nums[l] > target:
                    l = m+1
                else:
                    r = m-1
            else: ## right sorted array
                if target < nums[m] or nums[r] < target:
                    r = m-1
                else:
                    l = m+1
        return -1
            
#  [4,5,6,7,0,1,2]
#   l     m     r                 