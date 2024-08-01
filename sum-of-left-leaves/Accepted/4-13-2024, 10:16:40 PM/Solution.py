// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
      return not root.left and not root.right
        
      
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      
      return (root.left.val if root.left and self.isLeaf(root.left) else 0) + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)