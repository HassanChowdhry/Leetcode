// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        isFirstIter = True
        
        while fast and fast.next:
            if slow == fast and not isFirstIter:
                return True
            
            isFirstIter = False
            slow = slow.next
            fast = fast.next.next
        
        return False