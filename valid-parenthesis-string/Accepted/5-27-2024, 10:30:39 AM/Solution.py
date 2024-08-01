// https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return s[0]=='*'
        
        mp = {}
            
        def dfs(left, idx):
            if left < 0:
                return False
            if idx == n:
                return left==0
            if (left, idx) in mp:
                return mp[(left, idx)]
            
            if s[idx] == "(":
                res = dfs(left + 1, idx + 1)
            elif s[idx] == ")":
                res = dfs(left - 1, idx + 1)
            else:
                res = dfs(left + 1, idx + 1) or dfs(left - 1, idx + 1) or dfs(left, idx + 1)
                
            mp[(left, idx)] = res
            return res
        
        left = 0
        return dfs(left, 0)