// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        @cache
        def backtrack(num):
            if num in memo:
                return memo[num]
            if (num < 2):
                return 1
        
            res = backtrack(num - 2) + backtrack(num - 1)
            memo[num] = res
            return res
    
        return backtrack(n)