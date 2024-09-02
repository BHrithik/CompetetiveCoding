class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k%(sum(chalk))
        for i in range(0,len(chalk)):
            if chalk[i] > k:
                return i
            k = k-chalk[i]
