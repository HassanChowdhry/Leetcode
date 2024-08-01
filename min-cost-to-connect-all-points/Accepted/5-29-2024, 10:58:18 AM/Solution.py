// https://leetcode.com/problems/min-cost-to-connect-all-points

from heapq import heapify, heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen, minheap, curr, cost = set(), [], 0, 0
        seen.add(curr)
        heapify(minheap)

        for i in range(1, len(points)):
            dist = abs(points[curr][1]-points[i][1]) + abs(points[curr][0]-points[i][0])
            heappush(minheap, (dist, i))
        
        while len(seen)<len(points):
            d, pos = heappop(minheap)
            if pos in seen:
                continue
            seen.add(pos)
            cost += d

            for i in range(len(points)):
                if i in seen: continue
                dist = abs(points[pos][1]-points[i][1]) + abs(points[pos][0]-points[i][0])
                heappush(minheap, (dist, i))


        return cost


        