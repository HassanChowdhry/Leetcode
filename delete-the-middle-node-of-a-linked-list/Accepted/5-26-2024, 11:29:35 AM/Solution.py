// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        if head.next == None:
            return None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = head
        while prev.next != slow:
            prev = prev.next
        
        prev.next = prev.next.next
        return head