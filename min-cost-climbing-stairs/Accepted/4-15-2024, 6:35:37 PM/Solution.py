// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        @cache
        def backtrack(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            res = cost[i] + min(backtrack(i+1), backtrack(i+2))
            memo[i] = res
            return res
        
        return min(backtrack(1), backtrack(0))