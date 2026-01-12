class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTimeToEatBananas(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            t = getTimeToEatBananas(mid)

            if t <= h:
                res = mid
                r = mid - 1   # try smaller speed
            else:
                l = mid + 1   # need bigger speed

        return res