// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        start = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            curr = prices[i]

            if start > curr:
                start = curr
                continue

            diff = curr - start
            if diff > maxi:
                maxi = diff
        
        return maxi