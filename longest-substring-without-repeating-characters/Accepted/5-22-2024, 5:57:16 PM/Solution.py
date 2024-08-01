// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        n = len(s)        
        res = curr = l = r = 0

        while l < n and r < n:
            char = s[r]
            if char not in mp:
                mp[s[r]] = r
                curr+=1
                res = max(res, curr)
                r+=1
                continue
            
            while l <= r and char in mp:
                del mp[s[l]]
                l+=1
                curr-=1
            
            mp[s[r]] = r
            curr+=1
            res = max(res, curr)
            r+=1


        return res