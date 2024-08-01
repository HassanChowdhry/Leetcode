// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
                
            dfs(node.right)
            self.s += node.val
            node.val = self.s
            dfs(node.left)
        
        dfs(root)
        return root