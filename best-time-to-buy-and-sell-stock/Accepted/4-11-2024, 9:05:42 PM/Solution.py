// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        if len(prices) == 1:
            return 0

        maxi = prices[1] - prices[0]
        for i in range(1, len(prices)):
            curr = prices[i]

            if start > curr:
                start = curr
                continue

            diff = curr - start
            if diff > maxi:
                maxi = diff
        
        return maxi if maxi > 0 else 0