// https://leetcode.com/problems/find-center-of-star-graph

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(int)
        for v1, v2 in edges:
            adj[v1] += 1
            adj[v2] += 1

        n = len(adj)

        for edge in adj:
            if adj[edge] == n-1:
                return edge