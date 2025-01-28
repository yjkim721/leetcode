class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pnl = 0
        cur_price = prices[0]
        for price in prices[1:]:
            if cur_price < price:
                pnl += price - cur_price
            cur_price = price
        return pnl