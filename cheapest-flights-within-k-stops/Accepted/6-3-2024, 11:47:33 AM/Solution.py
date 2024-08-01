// https://leetcode.com/problems/cheapest-flights-within-k-stops

from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # edge list
        edges = defaultdict(list)
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmp = prices[::]
            for s, e, c in flights:
                if prices[s] == float("inf"): continue
                if prices[s]+c < tmp[e]:
                    tmp[e] = prices[s]+c
            prices = tmp

        
        return prices[dst] if prices[dst]!=float("inf") else -1

