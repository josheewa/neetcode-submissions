class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            res = max(res, prices[i]-buy)
        return res