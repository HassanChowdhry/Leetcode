// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        sign = False if x>0 else True
        curr = abs(x)
        while curr != 0:
            res *= 10
            carry = curr%10
            res += carry
            curr //= 10

        if -res < -2**31 or res > 2**31 - 1:
            return 0

        
        return res if not sign else -res