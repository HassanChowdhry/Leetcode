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
      i = 0
      while i < len(s):
        if s[i] in brackets:
          stack.append(s[i])
          sLen += 1
        elif sLen > 0 and brackets.get(stack[sLen - 1]) == s[i]:
          stack.pop()
          sLen -= 1
        else: 
          return False
        i += 1
            
      return sLen == 0