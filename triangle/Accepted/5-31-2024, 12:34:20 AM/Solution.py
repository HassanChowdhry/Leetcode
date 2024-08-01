// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # cache = {}
        N = len(triangle)

        @lru_cache(maxsize=None)
        def dfs(i, prev):
            if i >= N:
                return 0
            if prev >= len(triangle[i]):
                return 0
            # if (i, prev) in cache:
            #     return cache[(i, prev)]
            
            left = triangle[i][prev] + dfs(i+1, prev)
            right = triangle[i][prev] + dfs(i+1, prev+1)

            take = min(left, right)
            # cache[(i, prev)] = take
            return take
        
        return dfs(0, 0)