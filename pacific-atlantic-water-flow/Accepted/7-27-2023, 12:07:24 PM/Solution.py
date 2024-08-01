// https://leetcode.com/problems/pacific-atlantic-water-flow

# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
           # declare
      ROWS, COLS = len(heights), len(heights[0])
      ans = []
      pacific = set()
      atlantic = set()
      
      # logic
      def bfs(i, j, visit):
        queue = deque()
        queue.append((i, j))
        
        while queue:
          r, c = queue.popleft()
          
          for x, y in [(r, c), (r, c-1), (r, c+1), (r+1, c), (r-1, c)]: # goes right, down, left, up
            if (x, y) not in visit and x >= 0 and y >= 0 and x < ROWS and y < COLS and heights[x][y] >= heights[r][c]:
             queue.append((x, y))
             visit.add((x, y))
      
      # Main Loop
      for c in range(COLS):
        bfs(0, c, pacific)
        bfs(ROWS-1, c, atlantic)
        
      for r in range(ROWS):
        bfs(r, 0, pacific)
        bfs(r, COLS-1, atlantic)
      
      # return
      return list(pacific.intersection(atlantic))