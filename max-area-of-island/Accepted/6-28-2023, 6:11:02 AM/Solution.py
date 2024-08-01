// https://leetcode.com/problems/max-area-of-island

# https://leetcode.com/problems/max-area-of-island/

# Time O(mn), Space O(1)
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
      max = 0
      
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if grid[i][j] == 1:
            count = self.dfs(grid, i, j)
            max = count if max < count else max
      
      return max
    
    def dfs(self, grid: list[list[int]], i: int, j: int):
      if not self.inRange(grid, i, j) or grid[i][j] != 1:
        return 0      
      
      grid[i][j] = 2

      return 1 + self.dfs(grid, i, j + 1) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i - 1, j)
    
    
    def inRange(self, grid, i, j):
      return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i])