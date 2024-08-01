// https://leetcode.com/problems/coin-change

from math import inf, isinf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float("inf")] * (amount+1)
        res[0] = 0

        for i in range(amount+1):
            num = res[i]
            for coin in coins:
                if num>=0 and coin+i <= amount:
                    next_num = coin+i
                    res[next_num] = min(num+1, res[next_num])
        
        return res[-1] if res[-1] <= amount+1 else -1
