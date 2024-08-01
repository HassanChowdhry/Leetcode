// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

from heapq import heapify, heappop
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N % k:
            return False
        if k == 1:
            return True
        
        frq = Counter(nums)
        minheap = list(frq.keys())
        heapify(minheap)

        while minheap:
            peek = minheap[0]
            for i in range(peek, k+peek):
                if i not in frq:
                    return False
                
                frq[i]-=1
                if frq[i] == 0:
                    del frq[i]
                    if i == minheap[0]:
                        heappop(minheap)
        
        return True