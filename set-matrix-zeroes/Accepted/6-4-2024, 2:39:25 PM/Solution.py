// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        N = len(matrix)
        M = len(matrix[0])
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        
        def bfs(row, col, u, d, r, l):
            if row not in range(N) or col not in range(M):
                return
            matrix[row][col] = 0

            if u:
                bfs(row-1, col, u, d, r, l)
            elif d:
                bfs(row+1, col, u, d, r, l)
            elif r:
                bfs(row, col+1, u, d, r, l)
            elif l:
                bfs(row, col-1, u, d, r, l)

        
        for i, j in zeros:
            bfs(i, j, True, False, False, False)
            bfs(i, j, False, True, False, False)
            bfs(i, j, False, False, True, False)
            bfs(i, j, False, False, False, True)
            

