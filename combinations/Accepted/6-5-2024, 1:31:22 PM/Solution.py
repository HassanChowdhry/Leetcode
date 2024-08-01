// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(inner, i):
            if len(inner) == k:
                res.append(inner[::])
            

            for j in range(i+1, n+1):
                inner.append(j)
                backtrack(inner, j)
                inner.pop()
        
        backtrack([], 0)
        return res