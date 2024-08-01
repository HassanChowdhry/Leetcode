// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: list[TreeNode]) -> int:
      if not root:
        return 0
      
      res = []
      
      def findDiameter(root: TreeNode) -> int:
        if not root:
          return 0
        
        return 1 + max(findDiameter(root.left), findDiameter(root.right))
      
      def dfs(root: TreeNode):
        if not root:
          return
        
        diam = findDiameter(root.left) + findDiameter(root.right)
        res.append(diam)
        
        dfs(root.left)
        dfs(root.right)
          
              
      dfs(root)
      return max(res)