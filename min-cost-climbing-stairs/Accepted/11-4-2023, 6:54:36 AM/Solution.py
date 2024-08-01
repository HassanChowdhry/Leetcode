// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      return min(self.helper(cost, len(cost) - 1, {}), self.helper(cost, len(cost)-2, {}))
    
    def helper(self, cost, last, memo):
      if last == 0 or last == 1:
        return cost[last]
      
      if last in memo:
        return memo[last]
      
      res = cost[last] + min(self.helper(cost, last-1, memo), self.helper(cost, last-2, memo))

      memo[last] = res

      return res