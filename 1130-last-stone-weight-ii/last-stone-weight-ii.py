class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(i, delta):
            if i == len(stones):
                return abs(delta)
            return min(dp(i+1, delta-stones[i]), dp(i+1, delta+stones[i]))
        return dp(0, 0)