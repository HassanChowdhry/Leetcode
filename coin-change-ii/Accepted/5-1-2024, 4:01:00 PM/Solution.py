// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # combo sum of all possible ways
        memo = {}

        @lru_cache(maxsize=None)
        def dp(curr: int, prev: int):
            if curr == 0:
                return 1
            if (curr, prev) in memo:
                return memo[(curr, prev)]
            
            ways = 0
            for coin in coins:
                if coin <= curr and coin >= prev: 
                    take = dp(curr-coin, coin)
                    ways += take
            
            memo[(curr, prev)] = ways
            
            return ways
        
        ans = dp(amount, 0)
        return ans