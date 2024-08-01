// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        big, small = max(p.val, q.val), min(q.val, p.val)
        curr_val = root.val

        val_in_root = curr_val == big or curr_val == small
        root_between_val = curr_val < big and curr_val > small

        if val_in_root or root_between_val:
            return root

        return (
            self.lowestCommonAncestor(root.left, p, q) 
            if curr_val > big
            else self.lowestCommonAncestor(root.right, p, q)
        )