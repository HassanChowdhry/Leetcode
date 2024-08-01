// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        heapify(minheap)

        for head in lists:
            curr = head
            while curr:
                heappush(minheap, curr.val)
                curr = curr.next

        if not minheap:
            return None
        head = ListNode(heappop(minheap))
        curr = head
        while minheap:
            nxt = ListNode(heappop(minheap))
            curr.next = nxt
            curr = nxt
        
        return head