// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      nodeSet = set()
      curr = head
      
      while curr:
        if curr in nodeSet:
          return True
        
        nodeSet.add(curr)
        curr = curr.next
      
      return False