// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j <= len(t):
            if j == len(t):
                return 0
            
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                i+=1
        
        return len(t)-j