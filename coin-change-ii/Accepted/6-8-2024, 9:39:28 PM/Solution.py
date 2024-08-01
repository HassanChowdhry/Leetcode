// https://leetcode.com/problems/coin-change-ii

class Solution:
    def change(self, amount: int, c: List[int]) -> int:
        c.sort()
        cache = {}

        def dfs(curr, prev):
            if curr == 0:
                return 1
            if curr < 0:
                return 0
            if (curr, prev) in cache:
                return cache[(curr, prev)]
            
            ways = 0
            for coin in c:
                if coin >= prev and coin <= coin:
                    take = dfs(curr-coin, coin)
                    ways += take
            
            cache[(curr, prev)] = ways

            return ways
        
        return dfs(amount, 0)

