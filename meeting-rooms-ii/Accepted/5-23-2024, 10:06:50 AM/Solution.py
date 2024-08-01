// https://leetcode.com/problems/meeting-rooms-ii

from heapq import heapify, heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minheap = []
        heapify(minheap)

        arr = sorted(intervals)
        res = 0

        for start,end in arr:
            if len(minheap)==0:
                heappush(minheap, (end, 1))
                res = 1
                continue
            
            peek = minheap[0][0]
            if start >= peek:
                pair = heappop(minheap)
                heappush(minheap, (end,pair[1]))
                continue
            
            if start < peek:
                res += 1
                heappush(minheap, (end, res))
            
        return res