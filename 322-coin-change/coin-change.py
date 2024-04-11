class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        coins = coins[::-1]
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]
        
