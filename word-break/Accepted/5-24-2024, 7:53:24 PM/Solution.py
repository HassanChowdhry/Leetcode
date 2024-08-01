// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(len(s)+1)
        words = set(wordDict)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                sub = s[j:i]
                if s[j:i] in words and dp[j]:
                    dp[i] = True
        
        print(dp)
        return dp[-1]