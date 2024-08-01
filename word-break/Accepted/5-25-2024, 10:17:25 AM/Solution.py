// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        words = set(wordDict)

        maxlen = -1
        for word in words:
            maxlen = max(maxlen, len(word))

        for i in range(n):
            if not dp[i]:
                continue
            end = min(i+maxlen+1, n+1)
            
            for j in range(i+1, end):
                sub = s[i:j]
                if dp[i] and sub in words:
                    dp[j] = True

        print(dp)
        return dp[-1]