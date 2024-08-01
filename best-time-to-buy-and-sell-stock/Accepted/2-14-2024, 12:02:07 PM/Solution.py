// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        total_profit = 0
        buyDay = 0
        sellDay = 1

        while sellDay < len(prices):
            if prices[sellDay] < prices[buyDay]:
                buyDay = sellDay
                sellDay += 1
                continue
            
            profit = prices[sellDay] - prices[buyDay]

            if total_profit < profit:
                total_profit = profit
            
            sellDay+=1

        return total_profit