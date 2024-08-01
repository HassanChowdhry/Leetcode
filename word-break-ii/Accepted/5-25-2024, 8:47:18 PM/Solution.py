// https://leetcode.com/problems/word-break-ii

from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        dp = defaultdict(list)
        n = len(s)
        for start in range(n,-1,-1):
            inner = []
            for end in range(start, n):
                sub = s[start:end+1]
                if sub in wordDict:
                    if end == n-1:
                        inner.append(sub)
                    else:
                        curr = dp[end+1]
                        for c in curr:
                            w = sub + " " + c
                            inner.append(w)
                dp[start] = inner
        return dp[0]

