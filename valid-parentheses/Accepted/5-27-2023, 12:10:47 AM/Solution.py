// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:      
      # set maps for matching bracketss
      brackets = {
        '(':')',
        '[':']',
        '{':'}'
      }
      
      stack = [] # stack to store bracket
      sLen = 0
      for c in s:
        if c in brackets:
          stack.append(c)
          sLen += 1
        elif sLen > 0 and brackets.get(stack.pop()) == c:
          sLen -= 1
        else: 
          return False
            
      return sLen == 0