// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      fast = head
      slow = head

      if not slow.next:
        return None
      
      for i in range(n):
        fast = fast.next
        
      while fast and fast.next:
        fast = fast.next
        slow = slow.next
        
      if slow == head and fast == None:
        return head.next
      
      slow.next = slow.next.next
      return head