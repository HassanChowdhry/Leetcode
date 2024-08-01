// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        curr = k
        l = 0
        val = 1
        while curr > 0:
            if l == n-1:
                val = -1
            if l == 0:
                val = 1
            l += val            
            curr -= 1

        return l