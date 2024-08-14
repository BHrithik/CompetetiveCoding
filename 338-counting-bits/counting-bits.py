class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            res = 0
            n = i
            while n:
                res += n%2
                n = n>>1
            arr.append(res)
        return arr