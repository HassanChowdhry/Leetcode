// https://leetcode.com/problems/find-the-k-th-lucky-number

from collections import deque
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1
        
        ans = ""
        while k>1:
            ans = ''.join((("7" if k&1 else "4"), ans))
            k>>=1
        
        return ans
            