class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        low = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] > low:
                res += prices[i]-low
                low = prices[i]
        return res
