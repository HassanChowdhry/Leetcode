// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        visit = set()
        def dfs(i, j):
            if (i, j) in visit:
                return 
            visit.add((i, j))
            
            take = dfs(j, N-i-1)
            if take:
                x, y = take
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]
            return (i, j)
            
        
        for i in range(N-1):
            for j in range(i, N-i-1):
                dfs(i, j)