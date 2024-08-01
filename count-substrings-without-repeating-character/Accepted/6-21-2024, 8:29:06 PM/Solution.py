// https://leetcode.com/problems/count-substrings-without-repeating-character

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        stored = set()

        res, l, r = 0, 0, 0

        while r < len(s):
            while l < r and s[r] in stored:
                stored.remove(s[l])
                l+=1
            stored.add(s[r])
            res += (((r - l + 1) * 2) //2)
            r += 1
        return res