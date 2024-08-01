// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        w1 = list(word1)
        w2 = list(word2)

        # return 0
        def dfs(i, j, w1):
            if i==j==len(w1)==len(w2):
                return 0
            if i>=len(w1) or j>= len(w2):
                return abs(len(w2) - len(w1))
            string = ''.join(w1)
            if string in cache:
                return cache[string]
            
            if w1[i] == w2[j]:
                take = dfs(i+1, j+1, w1)
            else:
                # insert
                n1 = w1[::]
                n1.insert(i, w2[j])
                take = 1 + dfs(i+1, j+1, n1)

                # delete
                n1 = w1[::]
                n1.pop(i)
                take = min(take, 1+dfs(i, j, n1))
                
                # replace
                n1 = w1[::]
                n1[i] = w2[j]
                take = min(take, 1+dfs(i+1, j+1, n1))
            
            cache[string] = take
            return take            


        return dfs(0,0, w1)
    