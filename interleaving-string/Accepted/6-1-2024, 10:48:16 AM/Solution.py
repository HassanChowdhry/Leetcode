// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, M, L = len(s1), len(s2), len(s3)
        if N+M != L:
            return False
        
        cache = {}
        def dfs(i, j):
            if i+j >= L:
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            
            take = False
            if i<N and j< M and s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                take = any([dfs(i+1, j), dfs(i, j+1)])
            elif i<N and s1[i] == s3[i+j]:
                take = dfs(i+1, j)
            elif j<M and s2[j] == s3[i+j]:
                take = dfs(i, j+1)

            cache[(i, j)] = take
            return take
        
        return dfs(0, 0)