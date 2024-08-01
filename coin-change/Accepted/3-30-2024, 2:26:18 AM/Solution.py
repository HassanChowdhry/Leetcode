// https://leetcode.com/problems/coin-change

from math import inf, isinf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        for i in range(amount+1):
            memo[i] = inf
        
        memo[0] = 1
        @cache
        def dp(curr: int):
            if curr == 0:
                return 0
            if curr < 0:
                return inf
            if not isinf(memo[curr]):
                return memo[curr]
            
            min_coin = inf
            for coin in coins:
                min_coin = min(min_coin, 1 + dp(curr - coin))
            
            memo[curr] = min_coin
            return min_coin
        
        ans = dp(amount)
        return -1 if isinf(ans) else ans
