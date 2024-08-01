// https://leetcode.com/problems/number-of-islands

class Solution:
            # BFS - Time O(mn), Space O(n)
    def numIslands(self, grid: list[list[str]]) -> int:
      count = 0
      
      # traverses whole matrix
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if grid[i][j] == '1':
            self.bfs(grid, i, j)
            count += 1
      
      return count
    
    # help from youtube for dir part
    def bfs(self, grid: list[list[str]], i: int, j: int) -> None:
      queue = [[i, j]]
      directions = [0, 1, 0, -1, 0]
      
      while queue:
        r, c = queue.pop(0)
        for size in range(len(directions) - 1):
          nr, nc = r + directions[size], c + directions[size + 1]
          if self.inRange(grid, nr, nc) and grid[nr][nc] == '1':
            queue.append([nr, nc])
            grid[nr][nc] = 2
    
    def inRange(self, grid: list[list[str]], i: int, j: int):
      return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i])