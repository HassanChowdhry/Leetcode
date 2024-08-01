// https://leetcode.com/problems/ipo

from heapq import heappush, heapify, heappop
class Solution:
    def findMaximizedCapital(self, k: int, cap: int, p: List[int], c: List[int]) -> int:
        pairs = sorted(list(zip(c, p)))
        N = len(pairs)
        minheap = []
        heapify(minheap)

        capital = cap
        prev = 0
        while k > 0:
            k-=1
            i = prev
            while i < N and pairs[i][0] <= capital:
                heappush(minheap, -pairs[i][1])
                i+=1
            
            if not minheap:
                return capital

            prev = i
            capital += abs(heappop(minheap))

        return capital