// https://leetcode.com/problems/maximum-total-importance-of-roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edges = [[0, i] for i in range(n)]

        for v1, v2 in roads:
            edges[v1][0] += 1
            edges[v2][0] += 1
        
        edges.sort()
        cost_map = {}
        cost = 1
        for count, idx in edges:
            cost_map[idx] = cost
            cost += 1
        
        res = 0

        for v1, v2 in roads:
            res += cost_map[v1] + cost_map[v2]
        

        return res


