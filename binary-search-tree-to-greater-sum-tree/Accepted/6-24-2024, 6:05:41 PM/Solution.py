// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode, s = [0]) -> TreeNode:
        
        s = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            s[0] += node.val
            node.val = s[0]
            dfs(node.left)

            return
        
        dfs(root)
        return root