class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = []
        self.total = sum(w)
        iSum = 0
        for i in w:
            self.pre_sum.append(iSum+i)
            iSum = iSum+i
        print(f"generated arr = {self.pre_sum}")
        print(f"{self.pre_sum[-1]} {sum(w)}")
        # for i in range(0,len(w)):
        #     for j in range(0,self.weight[i]):
        #         self.arr.append(i)
        # print(f"generated arr = {self.arr}")

    def pickIndex(self) -> int:
        pick = random.randint(1, self.total) # or (1, self.pre_sum[-1])
        l = 0
        r = len(self.pre_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if pick <= self.pre_sum[mid]:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()