// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      num1 = ''
      num2 = ''

      while l1:
        num1 = str(l1.val) + num1
        l1 = l1.next

      while l2:
          num2 = str(l2.val) + num2
          l2 = l2.next

      num = int(num1) + int(num2)
      arr = list(str(num))

      l =  ListNode(arr[len(arr) - 1], None)
      curr = None
      prev = l

      for i in range(len(arr) - 2, -1, -1):
          curr = ListNode(arr[i], None)
          prev.next = curr
          prev = prev.next

      return l