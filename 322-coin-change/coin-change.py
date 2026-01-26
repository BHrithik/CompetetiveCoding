class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        def helper(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + helper(rem - coin))
            memo[rem] = res
            return res
        ans = helper(amount)
        return ans if ans != float('inf') else -1