// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set(i for i in range(n))
        adj_list = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        def dfs(root, prev):
            if root not in nodes:
                return
            nodes.remove(root)

            if root not in adj_list:
                return
            children = adj_list[root]
            for child in children:
                if prev != child:
                    dfs(child, root)
            
            return

        res = 0
        for i in range(n):
            if i in nodes:
                res += 1
                dfs(i, -1)
        return res