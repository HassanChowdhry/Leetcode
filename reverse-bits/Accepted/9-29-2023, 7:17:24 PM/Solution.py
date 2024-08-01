// https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0

        for i in range(32):
            bit = n % 2
            n >>= 1
            reverse = (reverse << 1) | bit
        
        return reverse