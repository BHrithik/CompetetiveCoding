class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        fin_res = float('inf')
        memo = {}
        def helper(rem_amt):
            if rem_amt > amount:
                return float('inf')
            if rem_amt == amount:
                return 0
            if rem_amt in memo:
                return memo[rem_amt]
            res = float('inf')
            for coin in coins:
                res = min(res, 1+helper(rem_amt+coin))
            memo[rem_amt] = res
            return res
        fin_res = helper(0)
        return fin_res if fin_res != float('inf') else -1