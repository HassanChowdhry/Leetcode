// https://leetcode.com/problems/min-cost-to-connect-all-points

from collections import defaultdict
from heapq import heapify, heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        minheap = []
        heapify(minheap)
        curr = 0
        seen.add(curr)

        for i in range(1, len(points)):
            dist = abs(points[i][1]-points[curr][1]) + abs(points[i][0]-points[curr][0])
            heappush(minheap, (dist, i))


        total = 0
        while len(seen) < len(points) and minheap:
            currdist, curr = heappop(minheap)        
            if curr in seen: continue
            seen.add(curr)
            total += currdist

            for i in range(len(points)):
                if i in seen: continue
                dist = abs(points[i][1]-points[curr][1]) + abs(points[i][0]-points[curr][0])
                heappush(minheap, (dist, i))
        
        return total

