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
            
            take = False
            if s[idx] == "(":
                take = dfs(left + 1, idx + 1)
            elif s[idx] == ")":
                take = dfs(left - 1, idx + 1)
            else:
                take = dfs(left + 1, idx + 1) or dfs(left - 1, idx + 1) or dfs(left, idx + 1)
                
            mp[(left, idx)] = take
            return take
        
        left = 0
        return dfs(left, 0)