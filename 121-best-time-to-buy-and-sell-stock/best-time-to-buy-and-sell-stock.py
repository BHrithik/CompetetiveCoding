class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        cur_price = prices[0]
        maxProfit = 0
        for i in prices[1:]:
            maxProfit = max(maxProfit,i-cur_price)
            cur_price = min(cur_price,i)
        return maxProfit
