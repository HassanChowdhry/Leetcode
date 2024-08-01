// https://leetcode.com/problems/surrounded-regions

# https://leetcode.com/problems/surrounded-regions/

from collections import deque


class Solution:
  # Time O(), Space O()
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # declare
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        
        # logic
        def dfs(i: int, j: int):
          if i < 0 or j < 0 or j >= COLS or i >= ROWS or board[i][j] == 'X' or (i, j) in visited:
            return
          
          visited.add((i, j))
          
          dfs(i + 1, j)
          dfs(i - 1, j)
          dfs(i, j + 1)
          dfs(i, j - 1)
        
        for i in range(ROWS):
          for j in range(COLS):
            if board[i][j] == 'O' and (i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1 ):
              dfs(i, j)
              
        for i in range(ROWS):
          for j in range(COLS):
            if board[i][j] == 'O' and (i, j) not in visited:
              board[i][j] = 'X'