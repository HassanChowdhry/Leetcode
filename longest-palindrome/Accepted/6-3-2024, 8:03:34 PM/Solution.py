// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frq = Counter(s)
        
        total = 0
        isOne = 0
        for letter in frq:
            if frq[letter] % 2 == 0:
                total += frq[letter]
            elif frq[letter] % 2 == 1:
                total += frq[letter] - 1
                isOne = 1
        return total+isOne

                