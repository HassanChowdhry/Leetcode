// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):
            if n==0: return 1

            if n < 0:
                return 1 / dfs(x, abs(n))
            
            if n % 2:
                return x * dfs(x * x, (n-1)/2)
            else:
                return dfs(x * x, n/2)
        
        return dfs(x, n)
            
