// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        N = len(triangle)

        
        def dfs(i, prev):
            if (i, prev) in cache:
                return cache[(i, prev)]
            curr = triangle[i][prev]
            
            if i < len(triangle)-1:
                curr += min(dfs(i+1, prev), dfs(i+1, prev+1))

            cache[(i, prev)] = curr
            return curr

            take = min(left, right)
            cache[(i, prev)] = take
            return take
        
        return dfs(0, 0)