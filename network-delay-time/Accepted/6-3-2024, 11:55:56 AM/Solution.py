// https://leetcode.com/problems/network-delay-time

from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap = []
        seen = set()
        edges = defaultdict(list)

        for s, e, c in times:
            edges[s].append((e, c))

        heapify(minheap)
        heappush(minheap, (0, k))

        total = 0
        while minheap:
            cost, start = heappop(minheap)
            if start in seen:
                continue
            seen.add(start)
            total = max(total, cost)
            for e, c in edges[start]:
                heappush(minheap, (cost+c, e))
        return total if len(seen)==n else -1