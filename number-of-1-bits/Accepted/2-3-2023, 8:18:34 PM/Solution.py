// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
      count = 0
      x = n
      while x > 0:
        count += (x & 1)
        x >>= 1
      return count