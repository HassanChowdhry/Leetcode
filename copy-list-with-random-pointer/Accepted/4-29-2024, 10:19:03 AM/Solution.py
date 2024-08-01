// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # new_map = {}
        idx_map = {}
        t_map = {}

        curr = head
        new_head = None
        prev = None
        idx = 0
        while curr:
            new_node = Node(curr.val, None, None)
            if prev: prev.next = new_node
            if idx == 0: new_head = new_node

            # new_map[new_node] = idx
            idx_map[idx] = new_node
            t_map[curr] = idx
            prev = new_node
            curr = curr.next
            idx+=1

        new_curr = new_head
        curr = head
        idx = 0

        while curr:
            if curr.random:
                ridx = t_map[curr.random]
                new_curr.random = idx_map[ridx]
            else:
                new_curr.random = None

            
            new_curr = new_curr.next
            curr = curr.next
        return new_head