// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            res = cost[i] + min(backtrack(i+1), backtrack(i+2))
            memo[i] = res 
            return res
        
        return min(backtrack(0), backtrack(1))