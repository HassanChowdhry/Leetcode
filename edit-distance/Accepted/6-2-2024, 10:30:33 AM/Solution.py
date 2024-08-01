// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if (i, j) in cache:
                return cache[(i, j)]
            
            if w1[i] == w2[j]:
                take = dfs(i-1, j-1)
            else:
                take = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
            
            cache[(i, j)] = take
            return take            


        return dfs(len(w1)-1, len(w2)-1)
    