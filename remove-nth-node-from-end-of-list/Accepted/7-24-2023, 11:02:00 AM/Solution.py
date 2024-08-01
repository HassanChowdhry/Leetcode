// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      curr = head
      length = 0
      while curr:
        length+=1
        curr = curr.next # B
      
      if length == 1:
        return None
      
      target = length - n - 1

      if target == -1:
        return head.next
      
      curr = head
      while target > 0:
        curr = curr.next
        target -= 1
      
      curr.next = curr.next.next
      
      return head