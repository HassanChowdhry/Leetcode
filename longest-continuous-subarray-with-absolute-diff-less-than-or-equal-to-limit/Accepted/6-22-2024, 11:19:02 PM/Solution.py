// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

from collections import deque
from heapq import heapify, heappop, heappush
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap, maxheap = [], []
        heapify(minheap)
        heapify(maxheap)

        heappush(minheap, (nums[0], 0))
        heappush(maxheap, (-nums[0], 0))
        
        res = 1
        l, r = 0, 1
        while r < len(nums):
            num = nums[r]

            heappush(minheap, (num, r))
            heappush(maxheap, (-num, r))

            while abs(minheap[0][0] - -maxheap[0][0]) > limit:
                l = min(minheap[0][1], maxheap[0][1]) + 1

                while minheap[0][1] < l:
                    heappop(minheap)
                while maxheap[0][1] < l:
                    heappop(maxheap)

            res = max(r - l + 1, res)
            r += 1
        
        return res
                





        
        return res

        