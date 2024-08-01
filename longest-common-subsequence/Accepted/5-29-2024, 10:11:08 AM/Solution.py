// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    if i-1 not in range(n) or j-1 not in range(m):
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    if i-1 not in range(n):
                        dp[i][j] = dp[i][j-1]
                    elif j-1 not in range(m):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp)  
        return dp[-1][-1]