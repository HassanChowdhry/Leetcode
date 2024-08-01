// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]*len(s)
        words = set(wordDict)
        for i in range(n):
            for j in range(n):
                if s[i:j+1] in wordDict:
                    dp[j] = 1
        res = set()
        @cache
        def dfs(string, idx):
            if (dp[idx] == 1 or dp[idx] == 2) and string in words:
                dp[idx] = 2
                res.add(string)
                string = ""
            
            for i in range(idx+1, n):
                string += s[i]
                dfs(string, i)
        
        dfs("", -1)
        
        return dp[-1] == 2