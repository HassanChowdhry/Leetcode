// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}

        @lru_cache(maxsize=None)
        def dfs(i, curr):
            if curr == target and i == N:
                return 1
            if i >= N:
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]

            ways = dfs(i+1, curr-nums[i]) + dfs(i+1, curr+nums[i])
            dp[(i, curr)] = ways
            return ways
        
        return dfs(0, 0)