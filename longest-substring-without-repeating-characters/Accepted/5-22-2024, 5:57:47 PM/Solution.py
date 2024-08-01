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
            
            mp[s[r]] = r
            curr+=1
            res = max(res, curr)
            r+=1


        return res