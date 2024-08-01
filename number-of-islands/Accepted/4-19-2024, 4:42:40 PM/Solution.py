// https://leetcode.com/problems/number-of-islands

class Solution:
    # BFS - Time O(mn), Space O(n)
    def numIslands(self, grid: list[list[str]]) -> int:
      count = 0
      
      def bfs(i: int, j: int ) -> None:
        # stores i, j in queue and list for direction change
        queue = deque()
        queue.append((i, j))
        
        while queue:
          r, c = queue.popleft()
          
          for x, y in [(r, c-1), (r, c+1), (r+1, c), (r-1, c)]:
            # goes right, down, left, up
            if x in range(len(grid)) and y in range(len(grid[i])) and grid[x][y] == '1':
              queue.append((x, y))
              grid[x][y] = 2 # change to recognize as visited
        
      # traverses whole matrix
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          # unvisited land
          if grid[i][j] == '1':
            bfs(i, j)
            count += 1
      
      return count