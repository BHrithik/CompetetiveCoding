class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            cur_sum = 0
            for j in range(i,n):
                cur_sum += nums[j]
                arr.append(cur_sum)
        arr.sort()
        res = (sum(arr[left-1:right]))%(10**9+7)
        return res