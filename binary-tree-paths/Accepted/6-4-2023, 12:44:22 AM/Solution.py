// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root: Optional[TreeNode]):
      return not root.left and not root.right
    
    def dfs(self, root: Optional[TreeNode], res: list, path: str):
      path += ("->" + str(root.val))
      if self.isLeaf(root):
        res.append(path)

      if root.left:
        self.dfs(root.left, res, path)
      if root.right:
        self.dfs(root.right, res, path) 
      
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      res = []
      
      if not root: 
        return res
      
      path = str(root.val)
      if self.isLeaf(root):
        res.append(path)
              
      if root.left:
        self.dfs(root.left, res, path)
      if root.right:
        self.dfs(root.right, res, path)

      return res