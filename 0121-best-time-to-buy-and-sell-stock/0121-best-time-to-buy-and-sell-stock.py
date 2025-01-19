class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n_prices = len(prices)
        if n_prices == 1:
            return 0

        max_n, max_idx = prices[0], 0
        min_n, min_idx = prices[0], 0
        profit = 0
        for i in range(1, n_prices):
            if prices[i] > min_n and prices[i] - min_n > profit:
                profit = prices[i] - min_n
            if prices[i] < min_n:
                min_n, min_idx = prices[i], i
            if prices[i] > max_n:
                max_n, max_idx = prices[i], i
        return profit                                                        

    def max(self, arr: List[int]) -> tuple[int, int]:
        max_val = 0
        max_idx = 0
        for i in range(len(arr)):
            if max_val < e:
                max_idx, max_val = i, e
        return max_idx, max_val

    def min(self, arr: List[int]) -> tuple[int, int]:
        min_val = 100000
        min_idx = 0
        for i in range(len(arr)):
            if min_val > e:
                min_idx, min_val = i, e
        return min_idx, min_val