// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def dfs(idx, buy):
            if idx >= N:
                return 0
            if (idx, buy) in dp:
                return dp[(idx, buy)]
            
            cool = dfs(idx+1, buy)
            if buy:
                profit = dfs(idx+1, not buy) - prices[idx]
                dp[(idx, buy)] = max(profit, cool)
            else:
                sell = dfs(idx+2, not buy) + prices[idx]
                dp[(idx, buy)] = max(sell, cool)

            return dp[(idx, buy)]

        return dfs(0, True)
