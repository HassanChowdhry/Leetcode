// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(row, col):
            if row==m-1 and col==n-1:
                return 1
            
            if row>=m or col >=n:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]
            
            res = dfs(row+1, col) + dfs(row, col+1)
            cache[(row, col)] = res
            return res

        return dfs(0,0)