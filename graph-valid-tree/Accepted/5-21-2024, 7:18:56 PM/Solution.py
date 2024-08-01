// https://leetcode.com/problems/graph-valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n==1:
            return True
        elif not edges and n>1:
            return False

        edges_map = {i:[] for i in range(n)}
        for edge1, edge2 in edges:
            edges_map[edge1].append(edge2)
            edges_map[edge2].append(edge1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            
            children = edges_map[i]
            for child in children:
                if child == prev:
                    continue
                if not dfs(child, i):
                    return False
            
            return True

        return dfs(0, -1) and len(visit)==n