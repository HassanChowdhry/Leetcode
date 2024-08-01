// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, left, down, right = float("inf"), float("inf"), float("-inf"), float("-inf")
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    top = min(top, r)
                    left = min(left, c)
                    down = max(down, r)
                    right = max(right, c)
        
        w = right-left+1
        l = down-top+1
        
        return w * l