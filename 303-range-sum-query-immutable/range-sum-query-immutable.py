class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur_sum = 0
        for i in nums:
            cur_sum += i
            self.prefix.append(cur_sum)
        print(self.prefix)

    def sumRange(self, l: int, r: int) -> int:
        lsum = self.prefix[l-1] if l > 0 else 0
        return self.prefix[r]-lsum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)