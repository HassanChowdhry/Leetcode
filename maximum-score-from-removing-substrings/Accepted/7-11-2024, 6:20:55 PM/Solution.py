// https://leetcode.com/problems/maximum-score-from-removing-substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) <= 1:
            return 0
        small, large = min(x, y), max(x, y)
        sub_small = "ab" if x < y else "ba"
        sub_large = "ab" if x > y else "ba"

        stack = []
        res = 0
        # first iteration - execute all large
        for c in s:
            if stack and (stack[-1]+c) == sub_large:
                stack.pop()
                res += large
            else:
                stack.append(c)
        
        ss = "".join(stack)
        stack = []

        # pop from stack and execute all small
        for c in ss:
            if stack and (stack[-1]+c) == sub_small:
                stack.pop()
                res += small
            else:
                stack.append(c)


        return res