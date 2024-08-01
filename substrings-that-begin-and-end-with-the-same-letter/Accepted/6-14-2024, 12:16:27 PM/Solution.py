// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum([ ((key * (key + 1)) // 2) for key in Counter(s).values() ])