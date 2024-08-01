// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x

        curr = abs(n)
        res = 1
        while curr > 0 :
            if curr % 2:
                res = res*x
                curr-=1

            x = x * x
            curr = curr // 2
        
        
        return res if n > 0 else 1/res
            
