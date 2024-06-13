class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        trib = [0,1,1]
        for i in range(3,n+1):
            ans = trib[0]+trib[1]+trib[2]
            trib[0] = trib[1]
            trib[1] = trib[2]
            trib[2] = ans
        return trib[2] 