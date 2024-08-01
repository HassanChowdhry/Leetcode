// https://leetcode.com/problems/rotting-oranges

class Solution:
  def orangesRotting(self, grid: list[list[int]]) -> int:
    # declare
    minutes = 0
    isPossible = True
    queue = deque()
      
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == 2:
          queue.append((i, j))

    def bfs() -> int:
      mins = 0
      
      while queue:
        size = len(queue)
        
        temp = 0
        for i in range(size):
          x, y = queue.popleft()
          
          for r, c in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
            if r in range(len(grid)) and c in range(len(grid[x])) and grid[r][c] == 1:
              queue.append((r, c))
              grid[r][c] = 2
              temp = 1
        
        mins += temp
      return mins
    
    minutes += bfs()
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == 1:
          isPossible = False    
          
    # return
    return -1 if not isPossible else minutes