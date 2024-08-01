// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
      # Declare
      max = 0
      
      # count area of an island
      def bfs(i: int, j: int) -> int:
        # declare
        queue = deque()
        queue.append((i, j))
        area = 0
        
        # counts area of an island, uses bfs
        while queue:
          r, c = queue.popleft()
          
          # goes right, down, left, up
          for x, y in [(r, c), (r, c-1), (r, c+1), (r+1, c), (r-1, c)]:
            if x in range(len(grid)) and y in range(len(grid[i])) and grid[x][y] == 1:
              queue.append((x, y))
              area += 1
              grid[x][y] = 2 # change to recognize as visited
        
        # return
        return area
      
      # check which island has most area
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if grid[i][j] == 1:
            count = bfs(i, j)
            max = count if max < count else max
      
      # return 
      return max