// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements

from heapq import heapify, heappush, heappop
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        minheap, maxheap = [], []
        heapify(minheap)
        heapify(maxheap)
        
        for num in nums:
            heappush(minheap, num)
            heappush(maxheap, -num)
        
        N = int(len(nums) /2)
        res = [0] * N
        i = 0
        while minheap and maxheap and i < N:
            maxx = -heappop(maxheap)
            minn = heappop(minheap)
            res[i] = ((maxx + minn)/2)
            i+=1
            
        
        
        
        return min(res)