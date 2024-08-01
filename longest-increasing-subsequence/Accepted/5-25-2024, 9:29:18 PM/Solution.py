// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*(n)
        mx = 1

        for start in range(n-1, -1, -1):
            for end in range(start, n):
                if nums[start] < nums[end]:
                    dp[start] = max(dp[start], dp[end]+1)
                    mx = max(mx, dp[start])
        return mx