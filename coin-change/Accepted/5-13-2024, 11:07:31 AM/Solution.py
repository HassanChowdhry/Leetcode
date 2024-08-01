// https://leetcode.com/problems/coin-change

from math import inf, isinf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float("inf")] * (amount+1)
        res[0] = 0

        for i in range(amount+1):
            num = res[i]
            if num>amount: continue
            for coin in coins:
                next_num = coin+i
                if next_num <= amount:
                    res[next_num] = min(num+1, res[next_num])
        
        return res[-1] if res[-1] <= amount else -1
