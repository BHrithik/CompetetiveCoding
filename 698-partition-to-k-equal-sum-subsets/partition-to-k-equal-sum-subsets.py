class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target_sum = total_sum//k
        if sum(nums)%k != 0 or max(nums) > target_sum:
            return False
        nums.sort(reverse= True)
        used = [False] * len(nums)
        def backTrack(start,k,cur_sum):
            if k == 0:
                return True
            if cur_sum == target_sum:
                return backTrack(0,k-1,0)
            for j in range(start,len(nums)):
                if used[j] or nums[j] + cur_sum > target_sum:
                    continue
                used[j] = True
                if backTrack(j+1, k, cur_sum+nums[j]):
                    return True
                used[j] = False
            return False
        return backTrack(0,k,0)