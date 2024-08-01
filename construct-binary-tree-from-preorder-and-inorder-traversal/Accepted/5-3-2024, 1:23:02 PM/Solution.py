// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # got logic, but needed help with code
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        root_idx_inorder = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_idx_inorder+1], inorder[:root_idx_inorder])
        root.right = self.buildTree(preorder[root_idx_inorder+1:], inorder[root_idx_inorder+1:])

        return root