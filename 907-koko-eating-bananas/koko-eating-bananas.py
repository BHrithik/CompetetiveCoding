class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            time = 0
            for i in piles:
                time += math.ceil(i/m)
            if time <= h:
                res = min(m,res)
                r = m-1
            else:
                l = m+1
        return res