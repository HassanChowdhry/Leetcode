// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int, seen = {}) -> int:
        if n in seen:
            return seen[n]
        
        res = 0
        
        if n == 0 or n == 1:
             res = n
        else:
            res = self.fib(n - 1, seen) + self.fib(n - 2, seen)
        
        seen[n] = res
                 
        return res