// https://leetcode.com/problems/most-profit-assigning-work

from heapq import heapify, heappop, heappush
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxheap = []
        heapify(maxheap)
        for p, d in zip(profit, difficulty):
            heappush(maxheap, (-p, d))
        if not maxheap: return 0
        
        total_profit = 0
        curr, level = heappop(maxheap)
        curr = abs(curr)
        for worker_level in sorted(worker, reverse=True):
            while maxheap and worker_level < level:
                curr, level = heappop(maxheap)
                curr = abs(curr)
            if not maxheap and worker_level < level: break
            total_profit += curr
            

        return total_profit