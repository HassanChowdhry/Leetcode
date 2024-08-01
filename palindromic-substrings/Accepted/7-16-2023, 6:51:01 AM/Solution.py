// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
      # declare
      count = len(s)
      visited = set()
      
      # checks if palindrome
      def isPalindrome(i, j):
        if i >= j:
          return True
        if s[i] != s[j]:
          return False
        
        return isPalindrome(i+1, j-1)
      
      # adds if in set or palindrom
      for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
          if s[i:j+1] in visited or isPalindrome(i, j):
            count += 1
            visited.add(s[i:j+1])
      
      # return
      return count