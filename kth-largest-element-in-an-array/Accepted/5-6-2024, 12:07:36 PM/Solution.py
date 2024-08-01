// https://leetcode.com/problems/kth-largest-element-in-an-array

from heapq import heappop, heappush, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_num = [-num for num in nums]
        heapify(rev_num)

        for i in range(k-1):
            heappop(rev_num)
        
        return -heappop(rev_num)
