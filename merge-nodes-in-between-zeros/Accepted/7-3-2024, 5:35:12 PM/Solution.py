// https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        while curr:
            while curr and curr.val != 0:
                prev.val += curr.val
                curr = curr.next
            if not curr or not curr.next: 
                prev.next = None
                break
            prev.next = curr
            prev = prev.next
            curr = curr.next
        
        return head