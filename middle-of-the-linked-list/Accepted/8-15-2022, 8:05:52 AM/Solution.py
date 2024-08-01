// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_size = 0
        node = head
        
        while node:
            list_size += 1
            node = node.next
        middle = (list_size // 2) 
        
        while head:
            if middle == 0:
                return head
            head = head.next
            middle -= 1