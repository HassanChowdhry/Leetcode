// https://leetcode.com/problems/hand-of-straights

from heapq import heapify, heappush, heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if groupSize == 1:
            return True
        if N % groupSize:
            return False
        
        frq = Counter(hand)
        minheap = list(frq.keys())
        heapify(minheap)

        while minheap:
            peek = minheap[0]

            for i in range(peek, peek+groupSize):
                if i not in frq:
                    return False
                frq[i]-=1
                if frq[i] == 0:
                    del frq[i]
                    if i == minheap[0]:
                        heappop(minheap)
        
        return True