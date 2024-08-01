// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: 
      curr = head
      prev = None
      while curr:
        if curr.val == val:
          if head == curr:
            head = head.next
            curr = head
          else:
            curr = curr.next
            prev.next = curr
        else:
          prev = curr
          curr = curr.next
      return head