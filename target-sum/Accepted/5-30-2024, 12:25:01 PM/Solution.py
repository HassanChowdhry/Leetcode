// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}

        def dfs(i, curr):
            if curr == target and i == N:
                return 1
            if (i, curr) in dp:
                return dp[(i, curr)]
            if i >= N:
                return 0

            dp[(i, curr)] = dfs(i+1, curr-nums[i]) + dfs(i+1, curr+nums[i])
            return dp[(i, curr)]
        
        return dfs(0, 0)