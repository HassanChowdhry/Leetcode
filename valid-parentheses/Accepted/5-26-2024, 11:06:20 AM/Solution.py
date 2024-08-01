// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:      
      
        # set maps for matching bracketss
        par = {
        '(':')',
        '[':']',
        '{':'}'
        }
        
        stack = [] # stack to store bracket

        for c in s:
            if c in par:
                stack.append(c)
            else:
                if len(stack)==0 or par[stack[-1]] != c:
                    return False
                stack.pop()

        return len(stack) == 0