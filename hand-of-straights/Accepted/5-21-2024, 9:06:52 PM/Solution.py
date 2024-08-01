// https://leetcode.com/problems/hand-of-straights

from heapq import heapify, heappush, heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        split = len(hand)//groupSize
        if groupSize == 1:
            return True
        if len(hand)%groupSize:
            return False
        
        frq = Counter(hand)
        minheap = list(frq.keys())
        heapify(minheap)

        while minheap:
            first = minheap[0]

            for i in range(first, first+groupSize):
                if i not in frq:
                    return False
                frq[i] -=1 
                if frq[i]==0:
                    if i != minheap[0]:
                        return False
                    heappop(minheap)
        return True