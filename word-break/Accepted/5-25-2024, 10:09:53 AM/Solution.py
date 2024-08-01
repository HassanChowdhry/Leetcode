// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        words = set(wordDict)

        for i in range(n):
            for j in range(1, n+1):
                sub = s[i:j]
                if dp[i] and sub in words:
                    dp[j] = True

        return dp[-1]