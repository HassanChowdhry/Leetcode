// https://leetcode.com/problems/maximum-repeating-substring

class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        N = len(word)
        if N > len(s):
            return 0
        if word == s:
            return 1
        
        rep = 1

        while word*(rep) in s:
            rep += 1
            
        return rep-1

