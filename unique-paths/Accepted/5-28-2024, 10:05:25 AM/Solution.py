// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        seen = set()

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row==m-1 and col==n-1: continue
                if (row, col) in seen: continue

                if row + 1 < m:
                    dp[row][col] += dp[row+1][col]
                if col + 1 < n:
                    dp[row][col] += dp[row][col+1]
                seen.add((row, col))

        return dp[0][0]