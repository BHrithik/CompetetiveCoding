class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(cur_amount):
            if cur_amount == 0:
                return 0
            if cur_amount < 0:
                return amount+1
            if cur_amount in cache:
                return cache[cur_amount]
            res = amount+1
            for coin in coins:
                res = min(res,helper(cur_amount-coin)+1)
            cache[cur_amount] = res
            return cache[cur_amount]
        res = helper(amount)
        return res if res != amount+1 else -1











        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a],1+dp[a-coin])
        return dp[amount] if dp[amount] != amount+1 else -1