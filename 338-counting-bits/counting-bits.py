class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            res = 0
            while i:
                res += i%2
                i = i>>1
            arr.append(res)
        return arr