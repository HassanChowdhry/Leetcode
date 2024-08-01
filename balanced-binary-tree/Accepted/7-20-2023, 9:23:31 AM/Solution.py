// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      if not root:
        return True
      
      def dfs(root, isBalanced):
        if not root:
          return 0
        
        left = dfs(root.left, isBalanced)
        right = dfs(root.right, isBalanced)
        
        isBalanced[0] &= (abs(left - right) <= 1)
        return 1 + max(left, right)
      
      isBalanced = [True]
      dfs(root, isBalanced)
      return isBalanced[0]