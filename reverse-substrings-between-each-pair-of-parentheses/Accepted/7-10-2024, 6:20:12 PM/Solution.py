// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "(":
                stack.append("R")
                stack.append("")
            elif c == ")":
                curr = stack.pop()
                curr = curr[::-1]
                stack.pop()
                if len(stack) > 0:
                    stack[-1] += curr
                else:
                    stack.append(curr)
            else:
                if len(stack) > 0:
                    stack[-1] += c
                else:
                    stack.append(c)
        
        return stack[0]