// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frq = Counter(s)
        
        total = 0
        isOne = 0
        for letter in frq:
            value = frq[letter]
            if value % 2 == 0:
                total += value
            elif value % 2 == 1:
                total += value - 1
                isOne = 1
        return total+isOne

                