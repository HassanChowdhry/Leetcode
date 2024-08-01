// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      if needle not in haystack:
        return -1
      
      for i, c in enumerate(haystack):
        if c == needle[0]:
          if haystack[i: i + len(needle)] == needle:
            return i