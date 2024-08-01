class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(ii, prod):
            if ii == len(nums): return

            self.mx = max(self.mx,
                prod * nums[ii], # case for continuing the subarray
                nums[ii], # case for starting a new subarry from ii
                prod # case for ending the subarry
            )
            dfs(ii + 1, prod * nums[ii])
            dfs(ii + 1, nums[ii])

        self.mx = nums[0]
        dfs(1, nums[0])
        return self.mx