// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        MAX_LETTERS = 26
        letters = {}
        res = 0

        l = 0
        for r in range(len(s)):
            letters[s[r]] = 1 + letters.get(s[r], 0)

            while (r - l + 1) - max(letters.values()) > k:
                letters[s[l]] -=1
                l+=1

            res = max(res, r - l + 1)
        return res