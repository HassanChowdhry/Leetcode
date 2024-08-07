// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # combo sum of all possible ways
        # memo = {}

        @cache
        def dp(curr: int, prev: int):
            # if curr in memo:
            #     return memo[curr]
            if curr == 0:
                return 1
            
            ways = 0
            for coin in coins:
                if coin <= curr and coin >= prev: 
                    take = dp(curr-coin, coin)
                    ways += take
            
            # memo[curr] = ways
            return ways
        
        ans = dp(amount, 0)
        return -1 if isinf(ans) else ans