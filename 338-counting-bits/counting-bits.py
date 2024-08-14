class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            res = 0
            n = i
            while n:
                n &= n-1
                res += 1
            arr.append(res)
        return arr