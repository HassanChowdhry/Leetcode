// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while len(queue) > 0:
            length = len(queue)
            level = []
            for i in range(length):
                curr_node = queue.pop(0)

                if not curr_node:
                    continue

                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)
                
            res.append(level)
        
        return res