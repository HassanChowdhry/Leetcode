// https://leetcode.com/problems/clear-digits

class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        stack = []

        for c in s:
            if c.isdigit() and stack:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)