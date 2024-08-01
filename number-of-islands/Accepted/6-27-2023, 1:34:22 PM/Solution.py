// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      visited = set()
      count = 0
      
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if str(i) + '-' + str(j) in visited or grid[i][j] == '0':
            continue
          count += self.helper(grid, visited, i, j)
      
      return count
    
    def helper(self, grid, visited, i, j):
      if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0' or str(i) + '-' + str(j) in visited:
            return 0

      visited.add(str(i) + '-' + str(j))

      
      self.helper(grid, visited, i, j + 1)
      self.helper(grid, visited, i + 1, j)

      self.helper(grid, visited, i, j - 1)
      self.helper(grid, visited, i - 1, j)

      return 1