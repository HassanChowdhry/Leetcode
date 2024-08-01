// https://leetcode.com/problems/walls-and-gates

# from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = []
        row = len(rooms)
        col = len(rooms[0])

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        def bfs():            
            mins = 1
            while queue:
                size = len(queue)
                
                for i in range(size):
                    x, y = queue.pop(0)
                
                    for r, c in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
                        if r in range(row) and c in range(col) and rooms[r][c]>0 and rooms[r][c]>mins:
                            queue.append((r, c))
                            rooms[r][c] = min(mins, rooms[r][c])    
                mins+=1
        bfs()
            