// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visit = set()
        N, M = len(matrix), len(matrix[0])
        
        def bfs(i, j, state):
            if len(res) == N*M:
                return
            if i not in range(N) or j not in range(M) or (i,j) in visit:
                if state == 'r':
                    bfs(i+1, j-1, 'd')
                elif state == 'l':
                    bfs(i-1, j+1, 'u')
                elif state == 'd':
                    bfs(i-1, j-1, 'l')
                elif state == 'u':
                    bfs(i+1, j+1, 'r')

                return
            visit.add((i, j))
            res.append(matrix[i][j])
            print(res)
            if state == 'r':
                bfs(i, j+1, state)
            elif state == 'l':
                bfs(i, j-1, state)
            elif state == 'd':
                bfs(i+1, j, state)
            elif state == 'u':
                bfs(i-1, j, state)
            
            return
            
        res = []
        bfs(0, 0, 'r')
        return res