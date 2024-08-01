// https://leetcode.com/problems/coin-change

from math import inf, isinf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        @cache
        def dp(curr: int):
            if curr in memo:
                return memo[curr]
            if curr == 0:
                return 0
            
            min_coin = inf
            for coin in coins:
                if coin <= curr: 
                    min_coin = min(min_coin, 1 + dp(curr - coin))
            
            memo[curr] = min_coin
            return min_coin
        
        ans = dp(amount)
        return -1 if isinf(ans) else ans
