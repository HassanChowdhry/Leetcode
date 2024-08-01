// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
      # declare
      carry = 0
      curr = ListNode()
      ans = curr
      
      # logic
      while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        sum = val1 + val2 + carry
        carry = sum // 10
        sum %= 10
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
        ans.val = sum
        if l1 or l2:
          ans.next = ListNode()
          ans = ans.next
        
      if carry:
        ans.next = ListNode(carry)  
      # return
      return curr