// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = [[float("-inf"), float("-inf")] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = float("-inf")
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0] + nums[i], dp[i-1][1] + nums[i])
            dp[i][1] = dp[i-1][0] - nums[i]
        
        
        return max(dp[-1])