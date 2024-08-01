// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        rem = set(nums)

        while head and head.val in rem:
            head = head.next
        
        curr = head
        while curr and curr.next:
            if curr.next.val in rem:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
