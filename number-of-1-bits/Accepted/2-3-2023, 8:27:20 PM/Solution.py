// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
      return 0 if n == 0 else (n & 1) + self.hammingWeight(n >> 1)
