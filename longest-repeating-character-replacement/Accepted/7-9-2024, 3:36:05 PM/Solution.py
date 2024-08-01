// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        res = 1
        for c in chars:
            l, r = 0, 0
            curr = 0
            curr_max = 1
            while r < len(s):
                if s[r] != c: 
                    while curr >= k and l <= r:
                        if s[l] != c:
                            curr -= 1
                        l += 1
                    curr += 1
                curr_max = max(curr_max, r-l+1)
                r += 1

            res = max(curr_max, res)
        return res