// https://leetcode.com/problems/network-delay-time

from collections import defaultdict
from heapq import heapify, heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap, seen = [], set()
        adj_list = defaultdict(list)
        for s, e, c in times: adj_list[s].append((e, c))
        heapify(minheap)
        heappush(minheap, (0, k))

        total = 0
        while minheap:
            cost, node = heappop(minheap)
            if node in seen: continue
            seen.add(node)
            total = max(total, cost)

            for nxt, c in adj_list[node]:
                if nxt in seen: continue
                heappush(minheap, (c+cost, nxt))
            del adj_list[node]
        
        return total if len(seen)==n else -1
