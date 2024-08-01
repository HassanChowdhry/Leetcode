// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        start = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            start = min(start, curr)
            maxi = max(maxi, curr-start)
        
        return maxi