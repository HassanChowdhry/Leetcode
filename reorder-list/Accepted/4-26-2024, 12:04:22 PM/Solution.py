// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        size = 1
        stack = []

        # find size of ll and set pointers to end and middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            size += 2
        
        if fast.next:
            fast = fast.next
            size += 1

        if size <= 2:
            return
        
        temp = slow
        slow = slow.next
        temp.next = None
        while slow:
            temp = slow
            stack.append(slow)
            slow = slow.next
            temp.next = None


        left = head 
        right = stack.pop()
        while len(stack) >= 0:
            temp = left.next
            left.next = right
            right.next = temp
            left = temp
            
            if len(stack) == 0:
                break
            
            right=stack.pop()
