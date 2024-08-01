// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room

class Solution:
    def minimumChairs(self, s: str) -> int:
        stack = []
        total = 0

        for i in range(len(s)):
            if s[i] == 'E':
                stack.append('E')
            elif s[i] == 'L':
                stack.pop()
            
            total = max(total, len(stack))
        
        return total