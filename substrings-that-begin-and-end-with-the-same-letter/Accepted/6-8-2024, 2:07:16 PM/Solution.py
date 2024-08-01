// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter

from math import factorial
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = Counter(s)
        
        res = 0
        for key in freq.values():

            res += ((key * (key + 1)) // 2)

        return res