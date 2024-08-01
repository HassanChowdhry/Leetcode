// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
      visited = set()
      count = 0
      
      # traverses whole matrix
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if self.coordinate(i, j) not in visited and grid[i][j] == '1':
            count += self.dfs(grid, visited, i, j)
      
      return count
    
    def dfs(self, grid: list[list[str]], visited: set, i: int, j: int) -> int:
      
      # checks out of bounds, alr visited and water
      if not self.inRange(grid, i, j) or grid[i][j] == '0' or self.coordinate(i, j) in visited:
            return 0

      visited.add(self.coordinate(i, j))
      
      self.dfs(grid, visited, i, j + 1) # right
      self.dfs(grid, visited, i + 1, j) # down

      self.dfs(grid, visited, i, j - 1) # left
      self.dfs(grid, visited, i - 1, j) # up

      return 1
    
    def coordinate(self, i: int, j: int) -> str:
      return str(i) + '-' + str(j)
    
    def inRange(self, grid, i, j):
      return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i])