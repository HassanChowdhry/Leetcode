// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        n = len(s)        
        res = curr = l = r = 0

        while l < n and r < n:
            char = s[r]
            while char in mp and l <= r:
                del mp[s[l]]
                l+=1
                curr-=1
            
            mp[char] = r
            curr+=1
            r+=1
            res = max(res, curr)


        return res