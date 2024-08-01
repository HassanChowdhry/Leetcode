// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def backtrack(i):
            if i >= len(cost):
                return 0
            
            res = cost[i] + min(backtrack(i+1), backtrack(i+2))
            return res
        
        return min(backtrack(1), backtrack(0))