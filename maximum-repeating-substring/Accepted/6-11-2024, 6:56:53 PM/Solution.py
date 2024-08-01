// https://leetcode.com/problems/maximum-repeating-substring

class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        N = len(word)
        if N > len(s):
            return 0
        if word == s:
            return 1
        
        rep = 0

        while word*(rep+1) in s:
            rep += 1
            
            
            
        return rep

