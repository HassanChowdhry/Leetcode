// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        seq = 0
        n = len(s)
        i = 0
        while i < n:
            curr = s[i]

            if curr not in mp:
                mp[curr] = i
                seq = max(seq, len(mp))
            else:
                i = mp[curr]
                mp = {}
            i+=1
        
        return seq