// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(2, n):
            temp = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = temp
        
        return t2