// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        reverse = head
        while reverse:
            reverse.val = stack.pop()
            reverse = reverse.next
        return head