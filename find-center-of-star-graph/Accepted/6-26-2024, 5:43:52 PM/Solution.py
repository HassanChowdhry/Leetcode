// https://leetcode.com/problems/find-center-of-star-graph

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(int)
        for v1, v2 in edges:
            if v1 in adj:
                return v1
            if v2 in adj:
                return v2
            adj[v1] += 1
            adj[v2] += 1