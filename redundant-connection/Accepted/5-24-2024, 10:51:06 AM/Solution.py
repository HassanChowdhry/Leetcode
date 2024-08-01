// https://leetcode.com/problems/redundant-connection

# REPEAT - UNION FIND
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        rank = [1 for i in range(N+1)]

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            
            return p

        def union(e1, e2):
            p1, p2 = find(e1), find(e2)

            if p1 == p2:
                return False
            

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]