// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            l , r = i, i+1
            curr = 1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                curr += 1
                l-=1
                r+=1
            
            l, r = i-1, i+1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                curr += 1
                l-=1
                r+=1
            
            res += curr
        
        return res