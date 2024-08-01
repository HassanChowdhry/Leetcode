// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if (n < 2):
            return 1
        
        res = self.climbStairs(n - 2, memo) + self.climbStairs(n - 1, memo)
        memo[n] = res
        return res