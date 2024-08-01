// https://leetcode.com/problems/k-closest-points-to-origin

from heapq import heappush, heappop, heapify
class Solution:
    # Time should be around O(nk)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # pqueue
        d = []
        m = {}
        heapify(d)
        for pair in points:
            x, y = pair
            dist = x**2 + y**2
            heappush(d, dist)
            
            if dist not in m:
                m[dist] = [pair]
            else:
                m[dist].append(pair)
                
        res = []
        for i in range(k):
            key = heappop(d)
            res.append(m[key].pop())
        return res