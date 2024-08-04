class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial_price = prices[0]
        profit = 0
        for i in prices[1:]:
            if initial_price > i:
                initial_price = i
            profit = max(profit, i-initial_price)
        return profit
