// https://leetcode.com/problems/pacific-atlantic-water-flow

# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # dfs
        # check surrounding for lower numbers
        # chose any possible path leading to the atlantic

        # declare
        vP = set()
        vA = set()
        ans = []

        # logic
        def dfsP(i: int, j: int):
            if (i, j) in vP:
              return False
            if i == 0 or j == 0:
              return True

            vP.add((i, j))

            check = False
            
            if heights[i][j] >= heights[i-1][j]:
              check |= dfsP(i-1, j)
            
            if heights[i][j] >= heights[i][j-1]:
              check |= dfsP(i, j-1)
            
            if i < len(heights)-1 and heights[i][j] >= heights[i+1][j]:
              check |= dfsP(i+1, j)
            
            if j < len(heights[i])-1 and heights[i][j] >= heights[i][j+1]:
              check |= dfsP(i, j+1)

            return check
        
        def dfsA(i: int, j: int):
            if (i, j) in vA:
              return False
            if i == len(heights)-1 or j == len(heights[i])-1:
              return True

            vA.add((i, j))

            check = False
            
            if heights[i][j] >= heights[i+1][j]:
              check |= dfsA(i+1, j)
            
            if heights[i][j] >= heights[i][j+1]:
              check |= dfsA(i, j+1)
            
            if i > 0 and heights[i][j] >= heights[i-1][j]:
              check |= dfsA(i-1, j)
            
            if j > 0 and heights[i][j] >= heights[i][j-1]:
              check |= dfsA(i, j-1)
            
            return check
            
        # main loop
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if dfsP(i, j) and dfsA(i, j):
                  ans.append([i, j])
                vA.clear()
                vP.clear()
        
        # return
        return ans