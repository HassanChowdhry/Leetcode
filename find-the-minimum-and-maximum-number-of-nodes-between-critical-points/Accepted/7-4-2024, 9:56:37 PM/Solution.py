// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []

        prev, curr = head, head.next
        dist = 0
        prevIsCritical = False
        i = first = 0
        while curr and curr.next:
            if (prev.val > curr.val < curr.next.val) or (prev.val < curr.val > curr.next.val):
                if prevIsCritical: 
                    res.append(dist)
                    res.append(i - first)
                else:
                    first = i
                dist = 0
                prevIsCritical = True

            if prevIsCritical: dist += 1
            prev = curr
            curr = curr.next
            i+=1
        return [min(res), max(res)] if len(res) >= 2 else [-1, -1]