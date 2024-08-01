// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome(text):
            return text == text[::-1]

        def backtrack(idx):
            if idx >= len(s):
                res.append(part.copy())
                return
            
            for i in range(idx, len(s)):
                sub = s[idx:i+1]
                if isPalindrome(sub):  
                    part.append(sub)
                    backtrack(i+1)
                    part.pop()

        backtrack(0)
        return res
        