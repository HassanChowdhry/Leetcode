// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        mp = defaultdict(int)
        curr = head
        while curr:
            mp[curr.val] += 1
            curr = curr.next

        curr = head
        while curr:
            if curr == head and mp[curr.val] > 1:
                head = head.next
                curr = head
                continue
            
            if curr.next and mp[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head