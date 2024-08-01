// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = [0 for _ in range(n)]
        adj = [[] for _ in range(n)]
        res = [[] for _ in range(n)]

        for src, dest in edges:
            neighbors[dest] += 1
            adj[src].append(dest)
        queue = deque()
        for i, l in enumerate(neighbors):
            if l == 0:
                queue.append(i)
        
        topnum = []
        while queue:
            curr = queue.popleft()
            topnum.append(curr)

            neig = adj[curr]
            for nm in neig:
                neighbors[nm]-=1
                if neighbors[nm] == 0:
                    queue.append(nm)

        unique = [set() for _ in range(n)]

        for num in topnum:
            for nm in adj[num]:
                unique[nm].add(num)
                unique[nm].update(unique[num])
        
        for i in range(n):
            res[i] += list(unique[i])
            res[i].sort()
        
        return res