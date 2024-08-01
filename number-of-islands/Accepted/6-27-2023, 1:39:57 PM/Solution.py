// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      visited = set()
      count = 0
      
      # traverses whole matrix
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if str(i) + '-' + str(j) not in visited and grid[i][j] == '1':
            count += self.dfs(grid, visited, i, j)
      
      return count
    
    def dfs(self, grid, visited, i, j):
      
      # checks out of bounds, alr visited and water
      if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0' or str(i) + '-' + str(j) in visited:
            return 0

      visited.add(str(i) + '-' + str(j))
      
      self.dfs(grid, visited, i, j + 1) # right
      self.dfs(grid, visited, i + 1, j) # down

      self.dfs(grid, visited, i, j - 1) # left
      self.dfs(grid, visited, i - 1, j) # up

      return 1